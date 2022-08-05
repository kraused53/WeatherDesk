# Used to gather user's location
import geocoder
# Used to get weather request
import requests
from SECRETS import OW_APIKEY
# Used to check if files exist
from os.path import exists
from SECRETS import PATH_TO_IMAGES
# Used to set the background image
import subprocess

'''

    Section 1: Get the user's location

        I will be using the geocoder library to use the user's IP address to 
        gather location information.

    return:
        Success -> [city, state, [lat, long]]
        Failure -> None
'''
def get_location():
    # geocoder.ip() returns lcoation information for a given IP address
    # 'me' tells geocoder to user the user's current IP address
    raw_location_information = geocoder.ip('me')

    # Variable to hold processed information
    location_information = None

    # Check for failed location search
    if raw_location_information is not None:
        location_information = []

        # Add user city to location data
        location_information.append(raw_location_information.city)
        # Add user state to location data
        location_information.append(raw_location_information.state)
        # Add user latitude and longitude to location data
        location_information.append(raw_location_information.latlng)

    return location_information


'''

    Section 2: Get a weather forecast

        I will be using the requests library to make an API call to the
        OpenWeatherAPI and extract the information I want

    return:
        Success -> [
            [current time],
            [sunrise],
            [sunset],
            [weather ID]
        ]
        Failure -> None

'''
def get_forecast(latlng):
    # Construct API request url
    API_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={key}&units=imperial'.format(lat=latlng[0], lng=latlng[1],key=OW_APIKEY)
    raw_weather_data = requests.get(API_URL)

    # Check for failed request
    if raw_weather_data.status_code != 200:
        return None
    
    # Convert to JSON
    raw_weather_data = raw_weather_data.json()
    
    weather_data = []

    # Check for time information
    if 'dt' in raw_weather_data:
        weather_data.append(raw_weather_data['dt'])
    else:
        weather_data.append(None)

    # Check for sunrise and sunset
    if 'sys' in raw_weather_data:
        if 'sunrise' in raw_weather_data['sys']:
            weather_data.append(raw_weather_data['sys']['sunrise'])
        else:
            weather_data.append(None)

        if 'sunset' in raw_weather_data['sys']:
            weather_data.append(raw_weather_data['sys']['sunset'])
        else:
            weather_data.append(None)
    else:
        weather_data.append(None)
        weather_data.append(None)
    
    # Check for weather ID
    if 'weather' in raw_weather_data:
        if 'id' in raw_weather_data['weather'][0]:
            weather_data.append(raw_weather_data['weather'][0]['id'])
        else:
            weather_data.append(None)
    else:
        weather_data.append(None)
    
    return weather_data


'''

    Step 3: Select an image

        This function takes the user's weather forecast and selects the 
        proper image

    return:
        Success -> [path to image, [errors]]
        Failure -> None

'''
def get_image_path(data):
    # set default time
    t = 'day'

    # If we have all time information
    if (data[2] is not None)and(data[2] is not None)and(data[2] is not None):
        # Determine time of day

        # Dawn if between sr - 2 hours and sr
        if (data[0] >= (data[1]- 7200)) and (data[0] < data[1]):
            t = 'dawn'
        # Morning if between sr and sr + 2 hours
        elif (data[0] >= data[1]) and (data[0] < (data[1]+ 7200)):
            t = 'morning'
        # Day if between sr + 2 hours and ss - 2 hours
        elif (data[0] >= (data[1]+ 7200)) and (data[0] < (data[2]- 7200)):
            t = 'day'
        # Evening
        elif (data[0] >= (data[2]- 7200)) and (data[0] < data[2]):
            t = 'evening'
        # Dusk
        elif (data[0] >= data[2]) and (data[0] < (data[2]+ 7200)):
            t = 'dusk'
        # Night
        else:
            t = 'night'

    # Check for weather code
    if data[3] is not None:
        weather_group = str(int(data[3] / 100) * 100)
    else:
        weather_group = '800'

    image_name = '/{wc}-{t}.jpg'.format(wc=str(data[3]), t=t)

    # Check for weather group folder
    path = PATH_TO_IMAGES + weather_group
    if exists(path):
        # Check for specific weather code
        if exists(path + '/' + str(data[3])):
            # Check for specific image
            if exists(path + '/' + str(data[3]) + image_name):
                return path + '/' + str(data[3]) + image_name
            # If the specific image does not exist, use default for group
            else:
                image_name = '/{wc}-{t}.jpg'.format(wc=weather_group, t=t)
                if exists(path + '/' + weather_group + image_name):
                    return path + '/' + weather_group + image_name
    
    # Check to see is
    return None

'''
    Everything below runs whenever main.py is run
'''
if __name__ == '__main__':
    # Step 1: Get user location
    location = get_location()

    print('Step 1: Get user location')
    print(location)
    print(' ')

    # Step 2: Get weather forecast
    forecast = get_forecast(location[2])
    print('Step 2: Get forecast')
    print(forecast)
    print(' ')

    # Step 3: Select an image
    image_path = get_image_path(forecast)
    print('Step 3: Select image')
    print(image_path)
    print(' ')

    # Step 4: Create image overlay
    print('Step 4: Create image overlay')
    print('SKIP FOR NOW')
    print(' ')

    # Step 5: Apply new desktop
    print('Step 5: Set background image')
    print(' ')
    subprocess.run(
        [
            '/usr/bin/gsettings', 
            'set', 
            'org.gnome.desktop.background', 
            'picture-uri', 
            image_path
        ], capture_output=True)