from location import get_location
from openweather import get_current_weather

if __name__ == '__main__':
    print('Fourth Step: Parse weather data.')

    # Use IP Geolocation to get Lat/Long estimate
    loc = get_location()

    # If get_location fails, exit program
    if loc is not None:
        print('You seem to be in ' + loc[0])
        print(loc[1])

        # Feed this Lat/Long into weather API
        weather = get_current_weather(loc[1])

        # Check for failed API call
        if weather is not None:
            # Parse JSON response
            
            # Define variables to fill
            current_time = None
            sunset = None
            sunrise = None
            weather_code = None

            # get weather code
            if 'weather' in weather:
                if 'id' in weather['weather'][0]:
                    weather_code = weather['weather'][0]['id']

            # get time of day
            if 'dt' in weather:
                current_time = weather['dt']

            if 'sys' in weather:
                # get sunset time
                if 'sunrise' in weather['sys']:
                    sunrise = weather['sys']['sunrise']
                # get sunrise time
                if 'sunset' in weather['sys']:
                    sunset = weather['sys']['sunset']

            print(current_time)
            print(sunset)
            print(sunrise)
            print(weather_code)

            # Generate file name based on weather and time of day

            # (OPTIONAL) Add text over image to display time and exact weather conditions

            # Apply new desktop
        else:
            print('ERROR: could not get a weather report')
    else:
        print('ERROR: could not get location')