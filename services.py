# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt


def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    print("-----------", c*r)
    return (c*r)


# "name":"Mangalore",
# "address":"Hotel Kamat",
# "lat":12.914142,
# "long":74.855957
#
# "name":"Udupi",
# "address":"Hotel Woodland",
# "lat":13.340881,
# "long":74.742142
#

# driver code
# lat1 = 13.340881
# lat2 = 12.914142
# lon1 = 74.742142
# lon2 = 74.855957
# print(distance(lat1, lat2, lon1, lon2), "K.M")