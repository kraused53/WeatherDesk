from location import LATITUDE, LONGITUDE
from weather_codes import *
import requests
import time

API_URL = (
        "https://api.open-meteo.com/v1/forecast?" +     # Base URL
        f"latitude={LATITUDE}&longitude={LONGITUDE}" +  # Location
        "&daily=sunrise,sunset" +                       # Get today's sunrise and sunset timestamps
        "&current=" +                                   # Current forecast
        "temperature_2m," +                             # Request temperature ( flaot )
        "is_day," +                                     # Request is it day ( bool )
        "weather_code," +                               # Request weather code ( int )
        "relative_humidity_2m" +                        # Request relative humidity ( int )
        "&wind_speed_unit=mph" +                        # Set wind speed units
        "&temperature_unit=fahrenheit" +                # Set temperature units
        "&precipitation_unit=inch" +                    # Set precipitation units
        "&timeformat=unixtime"                          # Set time format
)

def is_between( check, hi, lo ):
    if check > hi:
        return False
    elif check < lo:
        return False

    return True

def get_time_of_day( data ) -> str:
    # Get sunrise
    sunrise = -1
    if "daily" in data:
        if "sunrise" in data["daily"]:
            sunrise = int( data["daily"]["sunrise"][0] )

    # Get sunset
    sunset = -1
    if "daily" in data:
        if "sunset" in data["daily"]:
            sunset = int( data["daily"]["sunset"][0] )

    current_time = int( time.time() )

    # 3600 is 1 hour in UNIX timestamps, so 7200 is 2 hours
    if sunrise != -1 and sunset != -1:
        # If current time is within 2 hours of sunrise
        if is_between( current_time, sunrise + 7200, sunrise - 7200):
            # It is morning
            return "morning"

        # If current time is more than 2 hours past sunrise and less than 2 hours before sunset
        elif is_between( current_time, sunset - 7200, sunrise + 7200 ):
            # it is day time
            return "day"

        # If current time is more than 2 hours past sunrise and less than 2 hours before sunset
        elif is_between(current_time, sunset + 7200, sunset - 7200):
            # it is evening
            return "evening"

    else:
        # No sunrise / sunset data. return day
        return "day"

    # All other time must be night
    return "night"

def parse_weather(data) -> str:
    code = -1
    if "current" in data:
        if "weather_code" in data["current"]:
            code = int( data["current"]["weather_code"] )

    # No code found
    if code == -1:
        return "normal"

    if code in RAIN_CODES:
        return "rain"

    if code in SNOW_CODES:
        return "snow"

    if code in THUNDER_CODES:
        return "thunder"

    # All other codes normal
    return "normal"

if __name__ == '__main__':
    # Make API request
    raw_api_data = requests.get( API_URL )

    # validate response
    if raw_api_data.status_code != 200:
        print( f"Invalid API response code: {raw_api_data.status_code}" )
        exit( 1 )

    # Convert response into json
    json_data = raw_api_data.json()

    time_of_day = get_time_of_day( json_data )
    weather = parse_weather( json_data )

    print( time_of_day + "-" + weather + ".jpg" )