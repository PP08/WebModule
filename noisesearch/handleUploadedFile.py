import os
from django.conf import settings
import csv
from .models import Table_single, Sum_measurement_single
import pandas as pd
from datetime import datetime

def handle_uploaded_file(file_name):

    time_format = '%Y-%m-%d %H:%M:%S'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    file = pd.read_csv(file_path)

    latitude = file['Latitude'].mean()
    longitude = file['Longitude'].mean()
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], time_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)
    measurement_duration = end_time - start_time
    device_id = file['Device ID'][0]

    table_average_single = Sum_measurement_single(device_id=device_id, latitude=latitude, longitude=longitude,
                                                  average_spl_value=average_spl_value, measurement_duration=measurement_duration,
                                                  start_time=start_time, end_time=end_time)
    table_average_single.save()
    measurement_id = table_average_single.measurement_id

    # cr = csv.reader(open(file_path, 'rt'))
    # next(cr)
    # for row in cr:
    #     moment = datetime.strptime(row[1], time_format)
    #     spl_value = float(row[2])
    #     table_single = Table_single(device_id=device_id, latitude=latitude, longitude=longitude,
    #                                 spl_value=spl_value, measured_at=moment, measurement_id_id=measurement_id)
    #     table_single.save()

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], time_format)
        spl_value = float(file['Pressure'][i])
        table_single = Table_single(device_id=device_id, latitude=latitude, longitude=longitude,
                                    spl_value=spl_value, measured_at=moment, measurement_id_id=measurement_id)
        table_single.save()

