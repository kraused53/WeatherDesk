# Used to gather user's location
import geocoder
# Used to get weather request
import requests
from SECRETS import OW_APIKEY

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