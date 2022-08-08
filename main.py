# Used to gather user's location
import geocoder
# Used to get weather request
import requests
from SECRETS import OW_APIKEY
# Used to check if files exist
import os
from SECRETS import PATH_TO_IMAGES
# Used to edit found image
from PIL import Image, ImageDraw, ImageFont
# Used to set the background image
import subprocess

'''
    Section 1: Get the user's location

        I will be using the geocoder library to use the user's IP address to 
        gather location information.

    Inputs: None

    Return:
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

    Inputs:
        latlng -> [latitude, longitude]

    Return:
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
'''
'''
    This function will attempt to fin the given file in the given directory.
        It will search all sub-directories and return only the first instance
        of the given filename
    
    Inputs:
        filename -> (str) name of file to find
        path -> (str) full path to directory to be searched
    
    Return:
        Success -> path to fist instance of filename in path
        Failure -> None
'''
def find(filename, path):
    '''
        os.walk generates 3 items
            1] (str) the current root directory
            2] ([(str)]) A list of all directories found in root
            3] ([(str)]) A list of all non-directory items found in root
    '''
    for root, dirs, files, in os.walk(path):
        # Check to see if file has been found
        if filename in files:
            return os.path.join(root, filename)
    
    # If file is not found
    return None

'''
    This function will attempt to find an image that corresponds with 
        the given time and weather information

    return:
        Success -> path to image
        Failure -> path to default image

'''
def get_image_path(dt, sr, ss, wc):
    # set default time
    t = '-day'

    # If we have all time information
    if (dt is not None) and (sr is not None) and (ss is not None):
        # Determine time of day

        # Dawn if between sr - 2 hours and sr
        if (dt >= (sr- 7200)) and (dt < sr):
            t = '-dawn'
        # Morning if between sr and sr + 2 hours
        elif (dt >= sr) and (dt < (sr+ 7200)):
            t = '-morning'
        # Day if between sr + 2 hours and ss - 2 hours
        elif (dt >= (sr+ 7200)) and (dt < (ss- 7200)):
            t = '-day'
        # Evening
        elif (dt >= (ss- 7200)) and (dt < ss):
            t = '-evening'
        # Dusk
        elif (dt >= ss) and (dt < (ss+ 7200)):
            t = '-dusk'
        # Night
        else:
            t = '-night'

    # Convert weathercode into a string
    wc = str(wc)

    image_name = '/{wc}{t}.jpg'.format(wc=wc, t=t)

    # Try to find the genearated image
    fp = find(wc+t+'.jpg', PATH_TO_IMAGES)

    # If not found
    if fp is None:
        print('File not found, trying default for group...')
        # Try to find default image for this weather group
        image_name = '/{wc}00{t}.jpg'.format(wc=wc[0], t=t)
        fp = find(wc[0]+'00'+t+'.jpg', PATH_TO_IMAGES)

        # If not found
        if fp is None:
            print('File not found, returning system default...')
            # Return path to default image
            return PATH_TO_IMAGES+'800/800/800-day.jpg'
    
    # If file is found at any point, return the file path
    return fp

'''
    Everything below runs whenever main.py is run
'''
if __name__ == '__main__':
    # Step 1: Get user location
    location = get_location()
#    location = ['Evansville', 'Indiana', [37.9678, -87.4855]]
    print('Step 1: Get user location')
    print(location)
    print(' ')

    # Step 2: Get weather forecast
    wd = get_forecast(location[2])
#    wd = [1659984303, 1659956345, 1660006328, 801]
    print('Step 2: Get forecast')
    print(wd)
    print(' ')

    # Step 3: Select an image
    print('Step 3: Select image')
    image_path = get_image_path(wd[0], wd[1], wd[2], wd[3])
    print(image_path)
    print(' ')

    # Step 4: Create image overlay
    print('Step 4: Create image overlay')
    # Open a copy of the image
    im = Image.open(image_path)

    # Set up image for drawing
    draw = ImageDraw.Draw(im)

    # test line
    draw.rectangle(
        [(im.size[0]-400, im.size[1]-200), im.size],
        fill=(255, 255, 255),
        outline=(0, 0, 0),
        width=10,
        )

    # Generate text box
    forecast_text='City:  {city}\nState: {state}\nTime:  {time}'.format(
        city=location[0],
        state=location[1],
        time=wd[0]
        )

    f = ImageFont.truetype("DejaVuSans.ttf", 20)

    draw.text(
        (im.size[0]-400+15, im.size[1]-200+15),
        forecast_text,
        fill='black',
        font=f
    )

#    im.show()

    # Save the edited image in a new spot
    im.save(PATH_TO_IMAGES+'use-this-image.jpg')

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
            PATH_TO_IMAGES+'use-this-image.jpg'
        ], capture_output=True)