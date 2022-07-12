***WeatherDesk***

A simple python project to update my Ubuntu desktop background according to the weather at my current location.

# About

My inspiration for this project came from an old attempt at a weather forecast app that I made a while ago. I was browsing reddit one night and came across a really cool picture that someone took of a city street in the rain. I was thinking about how it would make a cool desktop background, and a light bulb went off! 

...

Unfortunately, a quick google search told me that I was not by any means the first person to have this idea. But, I really liked the idea and since my weather app idea had stalled I decided it would be a fun project anyway. 

As I was looking through other peoples take on the project, I came across the [WeatherDesk](https://github.com/bharadwaj-raju/WeatherDesk) project by GitHub user [bharadwaj-raju](https://github.com/bharadwaj-raju). They had a complete set of images based on the video game [FireWatch](https://www.firewatchgame.com/) that I fell in love with. 

![Image for a clear day](/images/day-clear.jpg)

I plan on expanding this project to cover more weather scenarios, so I will eventually replace these with a larger set of photos. But, these will always be one of my favorite sets.

# Program Flow

Here are the main steps this program follow:

1. Determine Location
2. Retrieve Weather Forecast
3. Parse Forecast and Select Proper File
4. ***TODO*** Add Header with Time, Location and Forecast to Image
5. Set Desktop Background

# Determine Location

One of the features I wanted to implement was automatic location estimation. This would mean that if the program was running on a laptop (like mine would be), the background would reflect the weather of the user's current location.

In order to implement this, I settled on the [geocoder library](https://geocoder.readthedocs.io/api.html). This library has several powerful geocoding capabilities, but it is really simple to use.

I have set up this program to use Geocoder to estimate the user's current location via their current IP address. So, as long as the user has an internet connection ad is not using a VPN, the program should be able to determine a reletivly accurate location.

# Retrieve Weather Forecast



# Parse Forecast and Select Image



# ***TODO*** : Add text to image



# Set Desktop Background

