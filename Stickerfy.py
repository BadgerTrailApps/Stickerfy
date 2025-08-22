from PIL import Image, ImageOps, ImageFilter
import sys

def stickerfy(image_path, output_path="sticker.png", border_color=(255, 255, 255), border_size=8, shadow_offset=3):
    # Load image and convert to RGBA.
    image = Image.open(image_path).convert("RGBA")

    # Remove transparency (auto-crop to content).
    bbox = image.getbbox()
    if bbox:
        image = image.crop(bbox)

    # Get image size.
    width, height = image.size

    # Resize to a maximum width or height of 464px.
    max_size = 464
    scale_factor = max_size / max(width, height)
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    image = image.resize((new_width, new_height), Image.LANCZOS)

    # Create a new 512x512 px sticker canvas.
    sticker_size = 512
    sticker = Image.new("RGBA", (sticker_size, sticker_size), (0, 0, 0, 0))
    offset_x = (sticker_size - new_width) // 2
    offset_y = (sticker_size - new_height) // 2
    sticker.paste(image, (offset_x, offset_y), image)

    # Create border mask.
    mask = image.split()[3]  # Extract alpha channel.
    expanded_mask = Image.new("L", (sticker_size, sticker_size), 0)
    expanded_mask.paste(mask, (offset_x, offset_y))

    # Upscale for smooth radial growth.
    scale = 4
    up_size = (sticker_size * scale, sticker_size * scale)
    mask_up = expanded_mask.resize(up_size, Image.LANCZOS)

    # Grow by blurring at higher resolution.
    blur_radius = border_size * scale * 0.6
    mask_up = mask_up.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert to binary again: anything not fully transparent gets max alpha. Creates sharp border edges after downscaling.
    thresholded = mask_up.point(lambda p: 255 if p > 0 else 0, mode='L')

    # Downscale back to sticker size with sharp edges.
    expanded_mask = thresholded.resize((sticker_size, sticker_size), Image.LANCZOS)

    # Create a solid border layer with the correct size.
    border = Image.new("RGBA", (sticker_size, sticker_size), border_color + (255,))
    border.putalpha(expanded_mask)

    # Add drop shadow.
    shadow = Image.new("RGBA", (sticker_size, sticker_size), (0, 0, 0, 0))
    shadow_mask = expanded_mask.filter(ImageFilter.GaussianBlur(3))
    shadow.paste((0, 0, 0, 100), (shadow_offset, shadow_offset), shadow_mask)

    # Merge all layers into the final sticker.
    final_sticker = Image.alpha_composite(shadow, border)
    final_sticker = Image.alpha_composite(final_sticker, sticker)

    # Save the final sticker.
    final_sticker.save(output_path, "PNG")
    print(f"✅ Sticker saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Provide an image!\ne.g.: python stickerfy.py image.png")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = input_path.replace(".png", "_stickerfy.png")
    stickerfy(input_path, output_path)
