from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from parse_weather_data import (
    get_current_time, 
    get_current_temperature, 
    get_current_humidity, 
    get_current_precipitation_probability
)
from datetime import datetime, timezone


# This function will take an image name and a dictionary of weather data to generate a
#   mini report and add it to the given image. The new image will be stored as
#   images/desktop.jpg
def make_desktop_image(img_title: str, data: dict, project_dir: Path, image_dir: Path, font_dir: Path) -> None:

    # Open image and create ImageDraw object
    image = Image.open(image_dir / img_title)
    draw = ImageDraw.Draw(image)

    # Get size and define box location
    w, h = image.size
    rect_coords = (w-425, h-225, w-20, h-20)
    rect_cent_x = ( rect_coords[2] + rect_coords[0] ) // 2
    rect_cent_y = ( rect_coords[3] + rect_coords[1] ) // 2


    # Load font
    try:
        font = ImageFont.truetype(font_dir / "SpaceMono.ttf", size=16)
    except IOError:
        # Fallback to the default system font if the file isn't found
        font = ImageFont.load_default()

    # Build image text
    current_time = datetime.fromtimestamp(get_current_time(data)).strftime("%I:%M %p")
    weather_text =  (
        "+==========================+\n" +
        f"| Time .......... {current_time} |\n"+
        "+==========================+\n" +
        f"| Temperature .... {get_current_temperature(data):3} °F |\n" +
        f"| Humidity .......... {get_current_humidity(data):2} % |\n" +
        f"| Precipitation ..... {get_current_precipitation_probability(data):2} % |\n" +
        "+==========================+\n"
    )

    text_box = draw.textbbox((0, 0), weather_text, font=font)
    text_cent_x = text_box[2] - text_box[0]
    text_cent_y = text_box[3] - text_box[1]

    text_x = rect_cent_x - text_cent_x // 2
    text_y = rect_cent_y - text_cent_y // 2

    # Add rectangle to image
    draw.rounded_rectangle(
        xy=rect_coords,
        radius=20,
        outline="Gray",
        fill="Silver",
        width=10
    )

    # Add text to rectangle
    draw.text((text_x, text_y), weather_text, fill="Black", font=font)

    # Save image
    image.save(image_dir / "desktop.jpg")