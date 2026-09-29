from PIL import Image, ImageDraw, ImageFont
from os import path
from parse_weather_data import *
from datetime import datetime, timezone


# This function will take an image name and a dictionary of weather data to generate a
#   mini report and add it to the given image. The new image will be stored as
#   images/desktop.jpg
def make_desktop_image(img_title: str, data: dict) -> None:
    working_dir = path.abspath(".")

    # Open image and create ImageDraw object
    image = Image.open(working_dir + "\\images\\" + img_title)
    draw = ImageDraw.Draw(image)

    # Get size and define box location
    w, h = image.size
    rect_coords = (w-620, h-220, w-20, h-20)
    rect_cent_x = ( rect_coords[2] + rect_coords[0] ) // 2
    rect_cent_y = ( rect_coords[3] + rect_coords[1] ) // 2


    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", size=24)
    except IOError:
        # Fallback to the default system font if the file isn't found
        font = ImageFont.load_default()

    # Build image text
    current_time = datetime.fromtimestamp(get_current_time(data)).strftime("%I:%M %p")
    weather_text = f"Time:  {current_time}"

    text_box = draw.textbbox((0, 0), weather_text, font=font)
    text_cent_x = text_box[2] - text_box[0]
    text_cent_y = text_box[3] - text_box[1]

    text_x = rect_cent_x - text_cent_x // 2
    text_y = rect_cent_y - text_cent_y // 2

    # Add rectangle to image
    draw.rounded_rectangle(
        xy=rect_coords,
        radius=20,
        outline="Black",
        fill="Gray",
        width=10
    )

    # Add text to rectangle
    draw.text((text_x, text_y), weather_text, fill="Black", font=font)

    # Save image
    image.save(working_dir + "\\images\\desktop.jpg")