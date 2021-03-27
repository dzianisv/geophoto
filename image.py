from PIL import Image, ImageFont, ImageDraw
import os

# https://towardsdatascience.com/reverse-geocoding-in-python-a915acf29eb6
def add_text(file_path, text):
    image = Image.open(file_path)
    title_font = ImageFont.truetype(
        os.path.join(os.path.dirname(__file__), 'Rajdhani-Medium.ttf'), 128
    )
    
    image_editable = ImageDraw.Draw(image)
    image_editable.text((100, image.height - 128 - 100), text, (255, 255, 255, 200), font=title_font)
    new_file_path = "geotagged_" + os.path.basename(file_path)
    image.save(new_file_path)
    origin_mtime = os.path.getmtime(file_path)
    os.utime(new_file_path, (origin_mtime, origin_mtime))