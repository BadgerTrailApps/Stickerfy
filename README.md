# Stickerfy.py 🦡

A simple Python tool to transform PNGs with transparency into a **512×512 px sticker** with a smooth border and subtle drop shadow — perfect for **Telegram, WhatsApp, Discord** and other sticker formats.

## Features
- **Automatic cropping** removes unnecessary transparency around your image
- **Smart resizing** keeps aspect ratio, max dimension 464px
- **Custom border** is adjustable size and color
- **Drop shadow** for the typical sticker effect
- **Ready-to-use size** with outputs exactly 512×512 px
- **Command-line friendly** to run it directly on your PNGs

## Installation
Install Python 3 and [Pillow](https://pillow.readthedocs.io/en/stable/):

```bash
pip install pillow
```

## Usage
```bash
python stickerfy.py image.png
```

```bash
python stickerfy.py image.png --output image_stickerfy.png --border_color 255 0 0 --border_size 12 --shadow_offset 5
```

## Example
![](example.png)
