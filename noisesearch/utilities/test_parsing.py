import os
from django.conf import settings
import pandas as pd
import csv




def handle_uploaded_file(file_path):

    # with open(os.path.join(settings.MEDIA_ROOT, file_name), 'rb') as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line)

    #table
    cr = csv.reader(open(file_path, 'rt'))
    next(cr)
    # for row in cr:
    #     print(row)

    file = pd.read_csv(file_path)
    # print(file['Latitude'].mean())



if __name__ == '__main__':
    handle_uploaded_file("/Users/phucphuong/Desktop/WebModule/media/documents/single/single-2017-04-07-03-14-53.csv")

    now = datetime.datetime.now()

    print(now)