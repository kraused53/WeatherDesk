from SECRETS import OW_APIKEY
from requests import get


'''
    get_current_weather(latlng):
        Uses a given latitude and longitude in the form:
            [lat, long]
        to retrieve a weather report for the given location.

        On success:
            return JSON data containing weather report
        On Fail:
            return None
'''
def get_current_weather(latlng):
    API_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={key}&units=imperial'.format(lat=latlng[0], lng=latlng[1],key=OW_APIKEY)
    weather_data = get(API_URL)

    # Check for failed get request
    if weather_data.status_code == 200:
        return weather_data.json()
    
    return None


if __name__ == '__main__':
    weather = print(get_current_weather([40.412, -86.937]))