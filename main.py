#!/usr/bin/env python

from location import get_location
from openweather import get_current_weather
from SECRETS import PATH_TO_IMAGES
import subprocess

"""
    get_filename(ct, ss, sr, wc):
        inputs
            ct -> current unix time (int)
            ss -> sunset unix time (int)
            sr -> sunrise unix time (int)
            wc  -> weather code (int)
        
        outputs
            success -> path to file with name
            failure -> path to day-clear.jpg

        This function takes parsed weather data and returns the correct 
            image file path
"""
def get_filename(ct, ss, sr, wc):
    # Create default time name
    t = 'day'

    # Create default weather name
    w = '-clear'

    # Check for complete time information
    if (ct is not None) and (ss is not None) and (sr is not None):
        # Determine time of day
        
        # Dawn if between sr - 2 hours and sr
        if (ct >= (sr - 7200)) and (ct < sr):
            t = 'dawn'
        # Morning if between sr and sr + 2 hours
        elif (ct >= sr) and (ct < (sr + 7200)):
            t = 'morning'
        # Day if between sr + 2 hours and ss - 2 hours
        elif (ct >= (sr + 7200)) and (ct < (ss - 7200)):
            t = 'day'
        # Evening
        elif (ct >= (ss - 7200)) and (ct < ss):
            t = 'evening'
        # Dusk
        elif (ct >= ss) and (ct < (ss + 7200)):
            t = 'dusk'
        # Night
        else:
            t = 'night'

    # Check for weather information
    if wc is not None:
        # Determine weather name

        # 200s -> Thunderstorm
        if (wc >= 200) and (wc < 300):
            w = '-thunder'
        # 300s and 500s -> Rain
        elif ((wc >= 300) and (wc < 400)) or ((wc >= 500) and (wc < 600)):
            w = '-rain'
        # 600s -> Snow
        elif (wc >= 600) and (wc < 700):
            w = '-snow'
        # All others display clear
        else:
            w = '-clear'

    return (PATH_TO_IMAGES + t + w + '.jpg')

if __name__ == '__main__':
    print('Sixth Step: Apply image to desktop.')

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

            # Generate file name based on weather and time of day
            filepath = get_filename(current_time, sunset, sunrise, weather_code)
            print(filepath)

            # (OPTIONAL) Add text over image to display time and exact weather conditions

            # Apply new desktop
            subprocess.run(['/usr/bin/gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', filepath], capture_output=True)
            print('\n\n')
            
        else:
            print('ERROR: could not get a weather report')
    else:
        print('ERROR: could not get location')
