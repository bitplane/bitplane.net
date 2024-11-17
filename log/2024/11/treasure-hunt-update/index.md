# 💸 treasure hunt update

Added [bitcoin treasure hunt](/log/2013/12/bitcoin-treasure-hunt) to the log
today, and couldn't read the grainy image and my shitty handwriting to get the
address.

So I used ChatGPT to help me brute-force the address from a list of candidates,

```python
import hashlib
from itertools import product

def verify_btc_checksum_safe(address):
    """
    Safely verify if a Bitcoin address has a valid checksum.
    """
    try:
        # Decode base58
        base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        base58_map = {char: index for index, char in enumerate(base58_chars)}

        # Convert the address to a number
        num = 0
        for char in address:
            num = num * 58 + base58_map[char]

        # Convert the number to bytes
        address_bytes = num.to_bytes(25, 'big')

        # The last 4 bytes are the checksum
        checksum = address_bytes[-4:]
        hashed = address_bytes[:-4]

        # Perform double SHA-256 on the address without the checksum
        valid_checksum = hashlib.sha256(hashlib.sha256(hashed).digest()).digest()[:4]

        # Compare calculated checksum to the actual checksum
        return checksum == valid_checksum
    except (ValueError, OverflowError, KeyError):
        return False

# Base58 character set
base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

# Ambiguous prefix with placeholders
prefix_template = "1E?hW???V?"
suffix = "8CCVLEQ9dMgCroJUcNGHMBot"

# Create a generator for address combinations
def generate_addresses(template, suffix, base58_chars):
    num_combinations = len(base58_chars) ** template.count("?")
    count = 0
    for chars in product(base58_chars, repeat=template.count("?")):
        address = template.replace("?", "{}").format(*chars) + suffix
        count += 1
        yield address, count, num_combinations

# Check and stream valid addresses
def find_valid_addresses():
    progress_step = 0.01  # Print progress every 1%
    last_progress = 0
    for address, count, total in generate_addresses(prefix_template, suffix, base58_chars):
        progress = count / total
        if progress >= last_progress + progress_step:
            print(f"Progress: {progress:.2%} ({count}/{total})")
            last_progress = progress
        if verify_btc_checksum_safe(address):
            print(f"Valid address found: {address}")
            break

# Run the generator and find valid addresses
if __name__ == "__main__":
    find_valid_addresses()
```

And found it:

```text
...
Progress: 88.00% (577593984/656356768)                                                                                                                                           
Progress: 89.00% (584157552/656356768)                                                                                                                                           
Progress: 90.00% (590721120/656356768)                                                                                                                                           
Valid address found: 1EuhWQkaVg8CCVLEQ9dMgCroJUcNGHMBot
```

[Nobody ever claimed it](https://www.blockchain.com/explorer/addresses/btc/1EuhWQkaVg8CCVLEQ9dMgCroJUcNGHMBot),
and it has a value of over £3k.

The hotel is now used to home asylum seekers, so will be refurbished or
demolished afterwards. If I was a braver man I'd go down there and offer bribes
to look in the rooms. But I'm not, and I'd imagine that security is pretty
tight given recent events and the fact it's in a rough area, I doubt I'd be
welcome!
