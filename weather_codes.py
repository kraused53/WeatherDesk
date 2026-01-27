# Sets for WMO weather codes [ https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM ]
# Anything not in the following 3 sets will be treated as "normal" for selecting an image
RAIN_CODES = (
    20, 21, 23, 24, 25,
    50, 51, 52, 53, 54,
    55, 56, 57, 58, 59,
    60, 61, 62, 63, 64,
    65, 66, 67, 68, 69,
    80, 81, 82, 83, 84,
    91, 92, 93, 94,
)

SNOW_CODES = (
    22, 26, 36, 37, 38,
    39, 70, 71, 72, 73,
    74, 75, 76, 77, 78,
    79, 85, 86, 87, 88,
    89, 90
)

THUNDER_CODES = (
    29, 95, 96, 97, 98,
    99
)