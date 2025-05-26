# 🎬 Asciicast Player

Plays an asciinema cast file encoded in the URL

<div id="status">It's not gonna work without JavaScript, is it?</div>
<div id="error"></div>
<div id="player-container" class="hidden"></div>

<div id="upload-container" class="hidden">
    <h2>Select or Paste Asciicast</h2>
    <input type="file" id="file-input" accept=".cast,.json">
    <textarea id="asciicast-input" placeholder="Paste asciicast data here..." rows="10"></textarea>
    <button id="go-button">GO!</button>
    <div id="link-container" class="hidden">
        <p>Shareable link:</p>
        <a id="share-link" href="#" target="_blank"></a>
        <p id="compression-stats" style="color: #888; font-size: 14px; margin-top: 10px;"></p>
    </div>
</div>

<link rel="stylesheet" href="/assets/css/asciinema-player.css">
<script src="/assets/js/asciinema-player.min.js"></script>
<script src="./asciicast-url.js"></script>
