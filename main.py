from location import get_location

if __name__ == '__main__':
    print('Second Step: Get user location.')

    # Use IP Geolocation to get Lat/Long estimate
    loc = get_location()

    # If get_location fails, exit program
    if loc is not None:
        print('You seem to be in ' + loc[0])
        print(loc[1])

        # Feed this Lat/Long into weather API

        # Parse JSON response

        # Generate file name based on weather and time of day

        # (OPTIONAL) Add text over image to display time and exact weather conditions

        # Apply new desktop
    else:
        print('ERROR: could not get location')