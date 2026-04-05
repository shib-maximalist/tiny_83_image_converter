# Tiny-83 Image Converter

A small tool that converts 22x14 pixel bitmap images into seed values for minting [Tiny-83 NFTs](https://opensea.io/collection/tiny-83). Because apparently everything can be an NFT — including a calculator screen.

## What it does

Takes a tiny black-and-white BMP image (22x14 pixels, 1-bit color depth) and encodes it as two 256-bit integers. These integers serve as the left and right seed values for on-chain minting.

**How the encoding works:**

1. The image gets split vertically into two 11x14 halves
2. Each pixel is assigned a power-of-2 weight based on its position
3. Black pixels contribute their weight, white pixels contribute nothing
4. The sum of all weights per half becomes the seed value

Essentially: `seed = Σ(pixel[i] × 2^i)` for i = 0 to 153. Simple binary encoding, but it maps visual patterns to blockchain-compatible integers — and stays within `uint256` limits.

## Usage

```bash
# Install dependencies
pip install numpy pillow

# Run the converter
python main.py
```

When prompted, enter the path to your BMP file. The script outputs two comma-separated integers ready to paste into the minting function.

```
Left:   21764133429535165757682873043452904982125215743
Right:  22835963083295327415964576320725097856141869054
CopyPaste for mint: 21764133429535165757682873043452904982125215743,22835963083295327415964576320725097856141869054
```

## Image requirements

- **Size:** 22x14 pixels exactly
- **Color depth:** 1-bit (black and white only)
- **Format:** BMP
- [Paint.NET](https://www.getpaint.net/) works well for creating these

## Dependencies

- Python 3.6+
- NumPy
- Pillow (PIL)

## Context

Built during the NFT era of 2021. The Tiny-83 project renders pixel art on a virtual TI-83 calculator screen — on-chain. This tool converts your pixel art into the seed values needed to mint it. Two sample images (`frog.bmp`, `ohm.bmp`) are included if you want to try it out.
