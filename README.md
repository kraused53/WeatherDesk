***WeatherDesk***

A simple python project to update my Ubuntu desktop background according to the weather at my current location.

# About

My inspiration for this project came from an old attempt at a weather forecast app that I made a while ago. I was browsing reddit one night and came across a really cool picture that someone took of a city street in the rain. I was thinking about how it would make a cool desktop background, and a light bulb went off! 

...

Unfortunately, a quick google search told me that I was not by any means the first person to have this idea. But, I really liked the idea and since my weather app idea had stalled I decided it would be a fun project anyway. 

As I was looking through other peoples take on the project, I came across the [WeatherDesk](https://github.com/bharadwaj-raju/WeatherDesk) project by GitHub user [bharadwaj-raju](https://github.com/bharadwaj-raju). They had a complete set of images based on the video game [FireWatch](https://www.firewatchgame.com/) that I fell in love with. 

![Image for a clear day](/images/day-clear.jpg)

I plan on expanding this project to cover more weather scenarios, so I will eventually replace these with a larger set of photos. But, these will always be one of my favorite sets.

# Basic Structure

## Project Layout

As of now, the files for this project are:
1. main.py
- The center piece of the program, it links all of the other functions together. Currently also contains the logic for selecting the correct background image.
2. location.py
- Contains the logic needed to estimate the user's current location.
3. openweather.py
- Contains the logic needed to find and retrieve a current weather report. 
4. ***NOT UPLOADED*** : SECRETS.py
- 
5. WeatherDesk.sh
- A bash file used to automate the program to run at regular intervals
6. ***DIRECTORY*** : images
- A directory holding all of the images used by this program

## Program Flow

1. Determine Location
2. Retrieve Weather Forecast
3. Parse Forecast and Select Proper File
4. ***TODO*** Add Header with Time, Location and Forecast to Image
5. Set Desktop Background

## Automation

In order to automate this program on my Linux PC (running Ubuntu 22.04 LTS) I created a bash file to be run by a CRON job. CRON is a standard automation software that now ships with Ubuntu installations. The bash file is needed in order to provide the python program with the context and PATH needed to execute properly.

# Location Estimation

One of the features I wanted to implement was automatic location estimation. This would mean that if the program was running on a laptop (like mine would be), the background would reflect the weather of the user's current location.

In order to implement this, I settled on the [geocoder library](https://geocoder.readthedocs.io/api.html). This library has several powerful geocoding capabilities, but it is really simple to use.

I have set up this program to use Geocoder to estimate the user's current location via their current IP address. So, as long as the user has an internet connection ad is not using a VPN, the program should be able to determine a relatively accurate location.

# Weather API

I am using the [Open Weather API](https://openweathermap.org/api) to gather weather forecasts. All that is required is a location (lattitude and longitude in my case) and an API key. In order to obtain an API key, you will need to register a free account. The API key should then be added to the (not uploaded) SECRETS.py file.

```python
# Example contents of SECRETS.py

# API Key from openweather
OW_APIKEY = "place key inside these quotes"

# FULL path from home directory to project images directory
PATH_TO_IMAGES = '/SOME/DIRECTORY/TO/PROJECT/WeatherDesk/images/'
```

# 


# ***TODO*** : Add text to image

