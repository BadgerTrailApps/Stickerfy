# Stickerfy.py 🎨✨

A simple Python tool to transform PNGs with transparency into a **512×512 px sticker** with a smooth border and subtle drop shadow — perfect for **Telegram, WhatsApp, Discord** and other sticker formats.

## Features
- **Automatic cropping** – removes unnecessary transparency around your image
- **Smart resizing** – keeps aspect ratio, max dimension 464px
- **Custom border** – adjustable size and color
- **Drop shadow** – for extra pop
- **Ready-to-use size** – outputs exactly 512×512 px
- **Command-line friendly** – run it directly on your images

## Installation

Install Python 3 and [Pillow](https://pillow.readthedocs.io/en/stable/):

```bash
pip install pillow

# Usage
Run the script with an image file as argument:

```bash
python stickerfy.py myimage.png

```bash
python stickerfy.py a.png --output my_sticker.png --border_color 255 0 0 --border_size 12 --shadow_offset 5
