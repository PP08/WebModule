import os
from django.conf import settings
import pandas as pd
import csv
from datetime import datetime
import math
from math import radians, sin, cos, sqrt, asin




def handle_uploaded_file(file_path):

    time_format = '%Y-%m-%d %H:%M:%S'
    # cr = csv.reader(open(file_path, 'rt'))
    # next(cr)
    # file = pd.read_csv(file_path)
    # start_time = datetime.strptime(file['Timestamp'][0], time_format)
    # end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)
    # print(end_time - start_time)
    file = pd.read_csv(file_path)

    # for i in range(len(file)):
    #     moment = datetime.strptime(file['Timestamp'][i], time_format)
    #     print(moment)

    latitudes = file['Latitude'].tolist()
    longitudes = file['Longitude'].tolist()

    # print(latitudes)

    points = [[i, j] for i, j in zip(latitudes, longitudes)]

    # print(points)
    return points



def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c



def cal_distance(points):
    """"""
    distance = 0
    for i in range(len(points) - 1):
        distance = distance + haversine(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])
    return distance


if __name__ == '__main__':
    points = handle_uploaded_file("/Users/phucphuong/Desktop/WebModule/media/documents/private/multiple/GotoCarousel.csv")
    print(cal_distance(points))


'''/Users/phucphuong/Desktop/WebModule/media/documents/private/multiple/GotoCarousel.csv'''
    #
    # now = datetime.now()
    # # cal_distance([48.72305363, 44.53600696], [48.7227573, 44.53632043])
    # print(haversine(48.7227550482707, 44.5363219273684, 48.72277377, 44.53632891) * 1000)
    #
    #
    # list_test = ['1', '2', '3', '4', '5']
    #
    #
    # print(list_test[0])
    #
    # input_string = '13 April, 2017'
    #
    # input_string = input_string.replace(',', '')
    #
    # date_array = input_string.split(' ')
    #
    # date_array = date_array[::-1]
    #
    # date_array = '-'.join(date_array) + ' 00:00:00'
    #
    # print(datetime.strptime(date_array, '%Y-%B-%d %H:%M:%S'))
    #
    #
    # # print(date_array)
    #
    # mydate = datetime.now()
    # # print (mydate.strftime("%B"))




