import os
from django.conf import settings
import csv
from .models import Table_single
import pandas as pd

def handle_uploaded_file(file_name):

    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    # with open(os.path.join(settings.MEDIA_ROOT, file_name), 'rb') as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line)

    #table
    table_single = Table_single()
    # cr = csv.reader(open(file_path, 'rt'))
    # for row in cr:
    #     # print(row)

    file = pd.read_csv(file_path)
    print(file[0])




