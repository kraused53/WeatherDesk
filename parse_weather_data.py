# Get current time
def get_current_time(data: dict) -> int:
    try:
        return data["current"]["time"]
    except KeyError:
        print("Could not find current time!")
        return -1

# Get sunrise time
def get_sunrise_time(data: dict) -> int:
    try:
        return data["daily"]["sunrise"][0]
    except KeyError:
        print("Could not find today's sunrise time!")
        return -1

# Get sunset time
def get_sunset_time(data: dict) -> int:
    try:
        return data["daily"]["sunset"][0]
    except KeyError:
        print("Could not find today's sunset time!")
        return -1

# Get current weather code
def get_current_weather_code(data: dict) -> int:
    try:
        return data["current"]["weather_code"]
    except KeyError:
        print("Could not find current weather code!")
        return -1

# Return the difference between two unix time stamps
def time_diff(a: int, b: int) -> int:
    return a - b

# Return a tring defined by the current time of day
def get_day_section(data: dict) -> str:
    # Get data
    ct = get_current_time(data)
    sr = get_sunrise_time(data)
    ss = get_sunset_time(data)

    # If there is an error, retur day
    # In case of full error, system will pick image day-normal.jpg
    if ct == -1 or sr == -1 or ss == -1:
        return "day"

    # Morning is +/- 1 hour from sunrise
    if abs(time_diff(ct, sr)) <= 3600:
        return "morning"

    # Day is 1 hour past sunrise to 1 hour before sunset
    if time_diff(ct, sr) > 3600 and time_diff(ct, ss) < -3600:
        return "day"
    
    # Evening is +/- 1 hour from sunset
    if abs(time_diff(ct, ss)) <= 3600:
        return "evening"

    # Night is all other times (less than 1 hour before sunrise or more than 1 hour after sunset)
    return "night"

WEATHER_TYPES = {
    51: "rain",
    53: "rain",
    55: "rain",
    56: "rain",
    57: "rain",

    61: "rain",
    63: "rain",
    65: "rain",
    66: "rain",
    67: "rain",

    71: "snow",
    73: "snow",
    75: "snow",
    77: "snow",

    80: "rain",
    81: "rain",
    82: "rain",

    85: "snow",
    86: "snow",

    95: "thunder",
    96: "thunder",
    97: "thunder",
    99: "thunder",
}

# Return a string description of the current weather data
def get_weather_type(data: dict) -> str:
    wc = get_current_weather_code(data)

    # If there is an error, retur normal
    # In case of full error, system will pick image day-normal.jpg
    if wc == -1:
        return "normal"

    return WEATHER_TYPES.get(wc, "normal")

# Get current temperature
def get_current_temperature(data: dict) -> float:
    try:
        return data["current"]["temperature_2m"]
    except KeyError:
        print("Could not find current temperature data")
        return 0.0

# Get current humidity
def get_current_humidity(data: dict) -> int:
    try:
        return int(data["current"]["relative_humidity_2m"])
    except KeyError:
        print("Could not find current humidity data")
        return 0

# Get current humidity

# Get current precipitation chance
def get_current_precipitation_probability(data: dict) -> int:
    try:
        return int(data["current"]["precipitation_probability"])
    except KeyError:
        print("Could not find current precipitation chance data")
        return 0