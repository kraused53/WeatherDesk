# Get current time
def get_current_time(data: dict) -> int:
    if "current_units" not in data or "time" not in data["current_units"]:
        print("Could not find units for current time!")
        return -1

    if data["current_units"]["time"] != "unixtime":
        print("Only unixtime stamps are supported!")
        return -1

    if "current" not in data or "time" not in data["current"]:
        print("Could not find report for current time!")
        return -1

    return data["current"]["time"]

# Get sunrise time
def get_sunrise_time(data: dict) -> int:
    if "daily_units" not in data or "time" not in data["daily_units"]:
            print("Could not find units for current temperature!")
            return -1

    if data["daily_units"]["time"] != "unixtime":
        print("Only unixtime stamps are supported!")
        return -1

    if "daily" not in data or "sunrise" not in data["daily"]:
        print("Could not find report for sunrise time!")
        return -1

    return data["daily"]["sunrise"][0]

# Get sunset time
def get_sunset_time(data: dict) -> int:
    if "daily_units" not in data or "time" not in data["daily_units"]:
            print("Could not find units for current temperature!")
            return -1

    if data["daily_units"]["time"] != "unixtime":
        print("Only unixtime stamps are supported!")
        return -1

    if "daily" not in data or "sunset" not in data["daily"]:
        print("Could not find report for sunset time!")
        return -1

    return data["daily"]["sunset"][0]

# Get current weather code
def get_current_weather_code(data: dict) -> int:
    if "current_units" not in data or "weather_code" not in data["current_units"]:
            print("Could not find units for current weather code!")
            return -1

    if data["current_units"]["weather_code"] != "wmo code":
        print("Only wmo codes are supported!")
        return -1

    if "current" not in data or "weather_code" not in data["current"]:
        print("Could not find report for current weather code!")
        return -1

    return data["current"]["weather_code"]

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

# Return a string description of the current weather data
def get_weather_type(data: dict) -> str:
    wc = get_current_weather_code(data)

    # If there is an error, retur normal
    # In case of full error, system will pick image day-normal.jpg
    if wc == -1:
        return "normal"

    print(wc)

    return "normal"

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
        return 0.0

# Get current humidity

# Get current precipitation chance
def get_current_precipitation_probability(data: dict) -> int:
    try:
        return int(data["current"]["precipitation_probability"])
    except KeyError:
        print("Could not find current precipitation chance data")
        return 0.0