***WeatherDesk***

A simple python project to update my Ubuntu desktop background according to the weather at my current location.

# About

My inspiration for this project came from an old attempt at a weather forecast app that I made a while ago. I was browsing reddit one night and came across a really cool picture that someone took of a city street in the rain. I was thinking about how it would make a cool desktop background, and a light bulb went off! 

...

Unfortunately, a quick google search told me that I was not by any means the first person to have this idea. But, I really liked the idea and since my weather app idea had stalled I decided it would be a fun project anyway. 

As I was looking through other peoples take on the project, I came across the [WeatherDesk](https://github.com/bharadwaj-raju/WeatherDesk) project by GitHub user [bharadwaj-raju](https://github.com/bharadwaj-raju). They had a complete set of images based on the video game [FireWatch](https://www.firewatchgame.com/) that I fell in love with. 

![Image for a clear day](/images/800/800/800-day.jpg)

I have several ideas that I still want to implement, so this repository is still subject to change.

# Program Flow

As of now, this program will follow consist of five steps:

## 1. Get user's location

I am using the Geocoder library to get an estimation of the user's current location. With a few lines of code, the Geocoder library can use the user's IP address to estimate lat/long and the city the user is nearest to.

## 2. Get weather forecast using this location

Once the program has gathered the user's location it will attempt to use the OpenWeather API to get a weather forecast. I am using the python requests library to make the API call and covert the response into a JSON package.

## 3. Use the weather forecast to select a background image

Using the time of day and the current weather conditions, the program will select the proper image from it's repository.

## 4. Make a copy of this image and overlay information from the forecast

Then, using the python image library (PIL or PILLOW) the program will overlay information from the forecast onto a copy of the image from step 3. This overlay will contain things like the current time, temperature and weather condition as well as an hourly future forecast

## 5. Set this new image as the desktop background

Finally, the program will set this new image as the computer's desktop background.