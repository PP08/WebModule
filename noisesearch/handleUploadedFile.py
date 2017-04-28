from .models import PrivateSingleAverage, PrivateSingleDetail, PublicSingleAverage, PublicSingleDetail, \
    PrivateMultipleAverage, PrivateMultipleDetail, PublicMultipleAverage, PublicMultipleDetail
import pandas as pd
from datetime import datetime
import json
from noisesearch.coordinates_helper import cal_distance

def save_private_data_single(file_path, username):

    time_format = '%Y-%m-%d %H:%M:%S'

    file = pd.read_csv(file_path)

    latitude = file['Latitude'].mean()
    longitude = file['Longitude'].mean()
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], time_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)
    measurement_duration = end_time - start_time
    device_id = file['Device ID'][0]

    private_single_average = PrivateSingleAverage(device_id=device_id, latitude=latitude, longitude=longitude,
                                                  average_spl=average_spl_value, duration=measurement_duration,
                                                  start_time=start_time, end_time=end_time, user_name=username)
    private_single_average.save()
    measurement_id = private_single_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], time_format)
        spl_value = float(file['Pressure'][i])
        private_single_detail = PrivateSingleDetail(device_id=device_id, latitude=latitude, longitude=longitude,
                                    spl_value=spl_value, measured_at=moment, measurement_id_id=measurement_id, user_name=username)
        private_single_detail.save()


def save_public_data_single(file_path, username):
    time_format = '%Y-%m-%d %H:%M:%S'

    file = pd.read_csv(file_path)

    latitude = file['Latitude'].mean()
    longitude = file['Longitude'].mean()
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], time_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)
    measurement_duration = end_time - start_time
    device_id = file['Device ID'][0]

    public_single_average = PublicSingleAverage(device_id=device_id, latitude=latitude, longitude=longitude,
                                                  average_spl=average_spl_value, duration=measurement_duration,
                                                  start_time=start_time, end_time=end_time, user_name=username)
    public_single_average.save()
    measurement_id = public_single_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], time_format)
        spl_value = float(file['Pressure'][i])
        public_single_detail = PublicSingleDetail(device_id=device_id, latitude=latitude, longitude=longitude,
                                                    spl_value=spl_value, measured_at=moment,
                                                    measurement_id_id=measurement_id, user_name=username)
        public_single_detail.save()



def save_private_data_multiple(file_path, username):
    """"""
    time_format = '%Y-%m-%d %H:%M:%S'
    file = pd.read_csv(file_path)

    device_id = file['Device ID'][0]
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], time_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)

    latitudes = file['Latitude'].tolist()
    longitudes = file['Longitude'].tolist()

    points = [[i, j] for i, j in zip(latitudes, longitudes)]
    distance = cal_distance(points)

    start_point = {'latitude': points[0][0], 'longitude': points[0][1]}
    end_point = {'latitude': points[-1][0], 'longitude': points[-1][1]}

    private_multiple_average = PrivateMultipleAverage(device_id=device_id, start_point= start_point, end_point=end_point,
                                                      average_spl=average_spl_value, distance=distance, start_time=start_time, end_time=end_time,
                                                      user_name=username)


    private_multiple_average.save()
    measurement_id = private_multiple_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], time_format)
        spl_value = float(file['Pressure'][i])
        private_multiple_detail = PrivateMultipleDetail(device_id=device_id, latitude=latitudes[i], longitude=longitudes[i],
                                    spl_value=spl_value, measured_at=moment, measurement_id_id=measurement_id, user_name=username)

        private_multiple_detail.save()


def save_public_data_multiple(file_path, username):
    """"""
    time_format = '%Y-%m-%d %H:%M:%S'
    file = pd.read_csv(file_path)

    device_id = file['Device ID'][0]
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], time_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], time_format)

    latitudes = file['Latitude'].tolist()
    longitudes = file['Longitude'].tolist()

    points = [[i, j] for i, j in zip(latitudes, longitudes)]
    distance = cal_distance(points)

    start_point = {'latitude': points[0][0], 'longitude': points[0][1]}
    end_point = {'latitude': points[-1][0], 'longitude': points[-1][1]}

    public_multiple_average = PublicMultipleAverage(device_id=device_id, start_point=start_point, end_point=end_point,
                                                      average_spl=average_spl_value, distance=distance,
                                                      start_time=start_time, end_time=end_time,
                                                      user_name=username)

    public_multiple_average.save()
    measurement_id = public_multiple_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], time_format)
        spl_value = float(file['Pressure'][i])
        public_multiple_detail = PublicMultipleDetail(device_id=device_id, latitude=latitudes[i],
                                                        longitude=longitudes[i],
                                                        spl_value=spl_value, measured_at=moment,
                                                        measurement_id_id=measurement_id, user_name=username)

        public_multiple_detail.save()
