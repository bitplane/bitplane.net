const statusEl = document.getElementById('status');
const errorEl = document.getElementById('error');
const playerContainer = document.getElementById('player-container');
const uploadContainer = document.getElementById('upload-container');
const asciicastInput = document.getElementById('asciicast-input');
const goButton = document.getElementById('go-button');
const shareLink = document.getElementById('share-link');
const fileInput = document.getElementById('file-input');

const BASE62_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

function base62Encode(bytes) {
    let num = 0n;
    for (let i = 0; i < bytes.length; i++) {
        num = (num << 8n) | BigInt(bytes[i]);
    }
    
    if (num === 0n) return '0';
    
    let result = '';
    while (num > 0n) {
        result = BASE62_CHARS[Number(num % 62n)] + result;
        num = num / 62n;
    }
    
    return result;
}

function base62Decode(str) {
    let result = 0n;
    
    for (let i = 0; i < str.length; i++) {
        result = result * 62n + BigInt(BASE62_CHARS.indexOf(str[i]));
    }
    
    const hex = result.toString(16).padStart(Math.ceil(result.toString(16).length / 2) * 2, '0');
    const bytes = new Uint8Array(hex.length / 2);
    for (let i = 0; i < hex.length; i += 2) {
        bytes[i/2] = parseInt(hex.substring(i, i+2), 16);
    }
    
    return bytes;
}

async function gzipCompress(text) {
    const encoder = new TextEncoder();
    const data = encoder.encode(text);
    
    const stream = new Response(data).body.pipeThrough(new CompressionStream('gzip'));
    const chunks = [];
    const reader = stream.getReader();
    
    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        chunks.push(value);
    }
    
    const totalLength = chunks.reduce((acc, chunk) => acc + chunk.length, 0);
    const result = new Uint8Array(totalLength);
    let offset = 0;
    for (const chunk of chunks) {
        result.set(chunk, offset);
        offset += chunk.length;
    }
    
    return result;
}

async function gzipDecompress(data) {
    const stream = new Response(data).body.pipeThrough(new DecompressionStream('gzip'));
    const chunks = [];
    const reader = stream.getReader();
    
    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        chunks.push(value);
    }
    
    const totalLength = chunks.reduce((acc, chunk) => acc + chunk.length, 0);
    const result = new Uint8Array(totalLength);
    let offset = 0;
    for (const chunk of chunks) {
        result.set(chunk, offset);
        offset += chunk.length;
    }
    
    return new TextDecoder().decode(result);
}

// Handle file selection
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;
    
    const reader = new FileReader();
    reader.onload = (e) => {
        asciicastInput.value = e.target.result;
    };
    reader.readAsText(file);
});

// Handle GO button click
goButton.addEventListener('click', async () => {
    const asciicastData = asciicastInput.value.trim();
    if (!asciicastData) {
        alert('Please upload a file or paste asciicast data');
        return;
    }
    
    try {
        // Validate it's proper asciicast format (first line should be valid JSON)
        const firstLine = asciicastData.split('\n')[0];
        JSON.parse(firstLine);
        
        const originalSize = new TextEncoder().encode(asciicastData).length;
        
        // Compress with gzip
        statusEl.textContent = 'gzip...';
        const compressed = await gzipCompress(asciicastData);
        
        const compressedSize = compressed.length;
        const ratio = ((1 - compressedSize / originalSize) * 100).toFixed(1);
        
        // Encode to base62
        statusEl.textContent = 'b62...';
        const encoded = base62Encode(compressed);
        
        // Use hash - no server limits
        const url = new URL(window.location);
        url.hash = encoded;
        
        const fullUrl = url.toString();
        
        // Warn if URL is too long
        if (fullUrl.length > 2048) {
            const urlKB = (fullUrl.length / 1024).toFixed(1);
            errorEl.textContent = `Warning: URL is ${urlKB}KB - may not work in all browsers!`;
            errorEl.style.display = 'block';
        }
        
        shareLink.href = fullUrl;
        shareLink.textContent = fullUrl.length > 75 ? fullUrl.substring(0, 75) + '...' : fullUrl;
        document.getElementById('compression-stats').textContent = `Original: ${(originalSize/1024).toFixed(1)}KB → Compressed: ${(compressedSize/1024).toFixed(1)}KB (${ratio}% reduction) → URL: ${(fullUrl.length/1024).toFixed(1)}KB`;
        document.getElementById('link-container').classList.remove('hidden');
        
        statusEl.textContent = '.';
    } catch (err) {
        errorEl.textContent = `Error: ${err.message}`;
        errorEl.style.display = 'block';
        statusEl.textContent = 'Something broke. Probably my fault.';
    }
});

// Main processing function
async function processAsciicast() {
    const castData = window.location.hash.substring(1);
    if (!castData) {
        statusEl.textContent = 'Gimme asciicast.';
        uploadContainer.classList.remove('hidden');
        
        // Try to load demo.cast
        fetch('./demo.cast')
            .then(response => {
                if (response.ok) {
                    return response.text();
                }
                throw new Error('demo.cast not found');
            })
            .then(data => {
                asciicastInput.value = data;
                statusEl.textContent = 'Demo loaded. Click GO to generate a shareable link.';
            })
            .catch(() => {
                // Silently ignore if demo.cast doesn't exist
            });
        
        return;
    }
    
    try {
        statusEl.textContent = 'Decoding base62 data...';
        const decodedData = base62Decode(castData);
        statusEl.textContent = 'Decompressing gzip data...';
        const decompressedText = await gzipDecompress(decodedData);
        
        // Create and initialize the asciinema player
        statusEl.textContent = 'Creating player...';
        playerContainer.classList.remove('hidden');
        
        // Clear any existing content
        playerContainer.innerHTML = '';
        
        // Create the player element
        const playerEl = document.createElement('div');
        playerEl.id = 'player';
        playerContainer.appendChild(playerEl);
        
        // Initialize the asciinema player with the asciicast data
        // The player expects a URL or a File/Blob object
        // Create a Blob from the asciicast text
        const blob = new Blob([decompressedText], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        
        AsciinemaPlayer.create(url, playerEl, {
            fit: 'width',
            autoPlay: true
        });
        
        // Clean up the object URL when done
        playerEl.addEventListener('destroy', () => {
            URL.revokeObjectURL(url);
        });
        
        statusEl.textContent = 'Playing asciicast.';
    } catch (err) {
        errorEl.textContent = `Error: ${err.message}`;
        errorEl.style.display = 'block';
        statusEl.textContent = 'Failed to process asciicast.';
        
        // Show upload container as fallback
        uploadContainer.classList.remove('hidden');
    }
}

// Start processing when the page loads
window.addEventListener('load', processAsciicast);
