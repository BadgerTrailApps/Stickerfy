# Stickerfy
This Python script is designed to turn images into sticker-like formats, adding a border, shadow, and resizing them to fit a 512x512px canvas - perfect for Telegram.

It works by removing transparency from images, expanding the alpha channel to create a clean border, and applying a drop shadow effect to give the sticker a 3D look.

## Requirements
* Python 3.x
* Pillow library (pip install pillow)

## Usage
Run the script with the following command:

```
python Stickerfy.py <image_path>
```

The script will then generate a new PNG file with the "_stickerfy" suffix.

## Example
![The original image.](/example.png)
![The result image.](/example_stickerfy.png)
