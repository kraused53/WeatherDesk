import os
from pathlib import Path
from dotenv import load_dotenv
import requests
import ctypes

from parse_weather_data import get_day_section, get_weather_type
from make_image import make_desktop_image

# Make an API request to open-meteo
def get_weather_data() -> dict:
    # Import environment secrets
    load_dotenv()

    params = {
        "latitude": os.getenv("LAT"),
        "longitude": os.getenv("LON"),
        "daily": "sunrise,sunset",
        "current": (
            "weather_code,"
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation_probability"
        ),
        "timezone": "auto",
        "forecast_days": 1,
        "timeformat": "unixtime",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }

    api_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params=params,
        timeout=10
    )

    # There was a problem with the API call, return None
    if api_response.status_code != 200:
        return None

    # Convert JSON data into Pyton dict
    return api_response.json()

# Apply selected image as wallpaper
def apply_wallpaper(img: str) -> None:
    # Constants for setting the wallpaper
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    if not os.path.isfile(img):
        raise FileNotFoundError(f"Wallpaper file not found: {img}")

    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        img,
        SPIF_UPDATEINIFILE | SPIF_SENDCHANGE,
    )

    if not result:
        error = ctypes.get_last_error()
        raise ctypes.WinError(error)

if __name__ == "__main__":
    PROJECT_DIR = Path(__file__).resolve().parent
    IMAGE_DIR = PROJECT_DIR / "images"
    FONT_DIR = PROJECT_DIR / "fonts"

    weather_data = get_weather_data()

    ds = get_day_section(weather_data)
    wt = get_weather_type(weather_data)

    file_name = f"{ds}-{wt}.jpg"

    make_desktop_image(file_name, weather_data, PROJECT_DIR, IMAGE_DIR, FONT_DIR)

    img = IMAGE_DIR / "desktop.jpg"
    apply_wallpaper(str(img))