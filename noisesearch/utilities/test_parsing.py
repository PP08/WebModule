import os
from django.conf import settings
import pandas as pd
import csv
from datetime import datetime
import math




def handle_uploaded_file(file_path):

    time_format = '%Y-%m-%d %H:%M:%S'
    cr = csv.reader(open(file_path, 'rt'))
    next(cr)
    file = pd.read_csv(file_path)
    start_time = datetime.strptime(file['Timestamp'][0], time_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)
    print(end_time - start_time)



def cal_distance(p1, p2):

    R = 6371e3

    lat1_rad = math.radians(p1[0])
    lat2_rad = math.radians(p2[0])

    delta_lat_rad = math.radians(p2[0] - p1[0])
    delta_long_rad = math.radians(p2[1] - p2[0])

    a = math.sin(delta_lat_rad) * math.sin(delta_lat_rad) + math.cos()



if __name__ == '__main__':
    handle_uploaded_file("/Users/phucphuong/Desktop/WebModule/media/documents/single/single-2017-04-07-03-14-53.csv")

    now = datetime.now()

    # t = datetime.strptime("2017-04-06 03:14:53", '%Y-%m-%d %H:%M:%S')
    #
    # print(now - t)