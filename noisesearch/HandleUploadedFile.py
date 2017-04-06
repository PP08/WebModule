import os
from django.conf import settings
import csv
from .models import Table_single
import pandas as pd
from datetime import datetime

def handle_uploaded_file(file_name):

    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    file = pd.read_csv(file_path)
    latitude = file['Latitude'].mean()
    longitude = file['Longitude'].mean()

    cr = csv.reader(open(file_path, 'rt'))
    next(cr)
    for row in cr:
        # print(row)
        device_id = row[0]
        moment = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        spl_value = float(row[2])
        table_single = Table_single(device_id=device_id, latitude=latitude, longitude=longitude, spl_value=spl_value, measured_at=moment)
        table_single.save()




