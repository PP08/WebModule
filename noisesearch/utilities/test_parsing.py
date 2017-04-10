import os
from django.conf import settings
import pandas as pd
import csv
from datetime import datetime
import math




def handle_uploaded_file(file_path):

    time_format = '%Y-%m-%d %H:%M:%S'
    # cr = csv.reader(open(file_path, 'rt'))
    # next(cr)
    # file = pd.read_csv(file_path)
    # start_time = datetime.strptime(file['Timestamp'][0], time_format)
    # end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)
    # print(end_time - start_time)
    file = pd.read_csv(file_path)

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], time_format)

        print(moment)


from math import radians, sin, cos, sqrt, asin


def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c





if __name__ == '__main__':
    handle_uploaded_file("/Users/phucphuong/Desktop/WebModule/media/documents/single/single-2017-04-07-03-14-53.csv")

    now = datetime.now()
    # cal_distance([48.72305363, 44.53600696], [48.7227573, 44.53632043])
    print(haversine(48.7227550482707, 44.5363219273684, 48.72277377, 44.53632891) * 1000)


    list_test = ['1', '2', '3', '4', '5']


    print(list_test[0])

