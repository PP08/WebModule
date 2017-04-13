from math import radians, sin, cos, sqrt, asin

from datetime import datetime

def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c * 1000

def detele_element(list, ids):

    detele_values = []
    for i in ids:
        detele_values.append(list[i])
    for value in detele_values:
        list.remove(value)

    return list

def convert_date_time(input_string):

    input_string = input_string.replace(',', '')

    date_array = input_string.split(' ')

    date_array = date_array[::-1]

    date_array = '-'.join(date_array) + ' 00:00:00'

    return (datetime.strptime(date_array, '%Y-%B-%d %H:%M:%S'))


