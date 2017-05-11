from .models import PrivateSingleAverage, PrivateSingleDetail, PublicSingleAverage, PublicSingleDetail, \
    PrivateMultipleAverage, PrivateMultipleDetail, PublicMultipleAverage, PublicMultipleDetail, TimeFilterPublicSingle, \
    TimeFilterPrivateSingle
import pandas as pd
from datetime import datetime
import json
from noisesearch.coordinates_helper import cal_distance

time_format = '%H:%M:%S'


def save_private_data_single(file_path, username):
    datetime_format = '%Y-%m-%d %H:%M:%S'

    file = pd.read_csv(file_path)

    latitude = file['Latitude'].mean()
    longitude = file['Longitude'].mean()
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], datetime_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], datetime_format)
    measurement_duration = end_time - start_time
    device_id = file['Device ID'][0]

    private_single_average = PrivateSingleAverage(device_id=device_id, latitude=latitude, longitude=longitude,
                                                  average_spl=average_spl_value, duration=measurement_duration,
                                                  start_time=start_time, end_time=end_time, user_name=username)
    private_single_average.save()
    measurement_id = private_single_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], datetime_format)
        spl_value = float(file['Pressure'][i])
        private_single_detail = PrivateSingleDetail(device_id=device_id, latitude=latitude, longitude=longitude,
                                                    spl_value=spl_value, measured_at=moment,
                                                    measurement_id_id=measurement_id, user_name=username)
        private_single_detail.save()

    ranges = divide_by_time(file)

    if (ranges[0][1] != 0):
        spl_value_0h_5h = round(file['Pressure'][ranges[0][0]: ranges[0][1]].mean(), 2)

    else:
        spl_value_0h_5h = 0.0

    if (ranges[1][1] != 0):
        spl_value_5h_10h = round(file['Pressure'][ranges[1][0]: ranges[1][1]].mean(), 2)
    else:
        spl_value_5h_10h = 0.0

    if (ranges[2][1] != 0):
        spl_value_10h_15h = round(file['Pressure'][ranges[2][0]: ranges[2][1]].mean(), 2)

    else:
        spl_value_10h_15h = 0.0

    if (ranges[3][1] != 0):
        spl_value_15h_20h = round(file['Pressure'][ranges[3][0]: ranges[3][1]].mean(), 2)
    else:
        spl_value_15h_20h = 0.0

    if (ranges[4][1] != 0):
        spl_value_20h_24h = round(file['Pressure'][ranges[4][0]: ranges[4][1]].mean(), 2)
    else:
        spl_value_20h_24h = 0.0

    devided_by_time_object = TimeFilterPrivateSingle(measurement_id_id=measurement_id, h0_h5=spl_value_0h_5h,
                                                     h5_h10=spl_value_5h_10h, h10_h15=spl_value_10h_15h,
                                                     h15_h20=spl_value_15h_20h, h20_h24=spl_value_20h_24h)

    devided_by_time_object.save()


def save_public_data_single(file_path, username):
    datetime_format = '%Y-%m-%d %H:%M:%S'

    file = pd.read_csv(file_path)

    latitude = file['Latitude'].mean()
    longitude = file['Longitude'].mean()
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], datetime_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], datetime_format)
    measurement_duration = end_time - start_time
    device_id = file['Device ID'][0]

    public_single_average = PublicSingleAverage(device_id=device_id, latitude=latitude, longitude=longitude,
                                                average_spl=average_spl_value, duration=measurement_duration,
                                                start_time=start_time, end_time=end_time, user_name=username)
    public_single_average.save()
    measurement_id = public_single_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], datetime_format)
        spl_value = float(file['Pressure'][i])
        public_single_detail = PublicSingleDetail(device_id=device_id, latitude=latitude, longitude=longitude,
                                                  spl_value=spl_value, measured_at=moment,
                                                  measurement_id_id=measurement_id, user_name=username)
        public_single_detail.save()

    ranges = divide_by_time(file)

    if (ranges[0][1] != 0):
        spl_value_0h_5h = round(file['Pressure'][ranges[0][0]: ranges[0][1]].mean(), 2)

    else:
        spl_value_0h_5h = 0.0

    if (ranges[1][1] != 0):
        spl_value_5h_10h = round(file['Pressure'][ranges[1][0]: ranges[1][1]].mean(), 2)
    else:
        spl_value_5h_10h = 0.0

    if (ranges[2][1] != 0):
        spl_value_10h_15h = round(file['Pressure'][ranges[2][0]: ranges[2][1]].mean(), 2)

    else:
        spl_value_10h_15h = 0.0

    if (ranges[3][1] != 0):
        spl_value_15h_20h = round(file['Pressure'][ranges[3][0]: ranges[3][1]].mean(), 2)
    else:
        spl_value_15h_20h = 0.0

    if (ranges[4][1] != 0):
        spl_value_20h_24h = round(file['Pressure'][ranges[4][0]: ranges[4][1]].mean(), 2)
    else:
        spl_value_20h_24h = 0.0

    devided_by_time_object = TimeFilterPublicSingle(measurement_id_id=measurement_id, h0_h5=spl_value_0h_5h,
                                                    h5_h10=spl_value_5h_10h, h10_h15=spl_value_10h_15h,
                                                    h15_h20=spl_value_15h_20h, h20_h24=spl_value_20h_24h)

    devided_by_time_object.save()

    # print(spl_value_20h_24h)


def save_private_data_multiple(file_path, username):
    """"""
    datetime_format = '%Y-%m-%d %H:%M:%S'
    file = pd.read_csv(file_path)

    device_id = file['Device ID'][0]
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], datetime_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], datetime_format)

    latitudes = file['Latitude'].tolist()
    longitudes = file['Longitude'].tolist()

    points = [[i, j] for i, j in zip(latitudes, longitudes)]
    distance = cal_distance(points)

    start_point = {'latitude': points[0][0], 'longitude': points[0][1]}
    end_point = {'latitude': points[-1][0], 'longitude': points[-1][1]}

    private_multiple_average = PrivateMultipleAverage(device_id=device_id, start_point=start_point, end_point=end_point,
                                                      average_spl=average_spl_value, distance=distance,
                                                      start_time=start_time, end_time=end_time,
                                                      user_name=username)

    private_multiple_average.save()
    measurement_id = private_multiple_average.id

    for i in range(len(file)):
        moment = datetime.strptime(file['Timestamp'][i], datetime_format)
        spl_value = float(file['Pressure'][i])
        private_multiple_detail = PrivateMultipleDetail(device_id=device_id, latitude=latitudes[i],
                                                        longitude=longitudes[i],
                                                        spl_value=spl_value, measured_at=moment,
                                                        measurement_id_id=measurement_id, user_name=username)

        private_multiple_detail.save()


def save_public_data_multiple(file_path, username):
    """"""
    datetime_format = '%Y-%m-%d %H:%M:%S'
    file = pd.read_csv(file_path)

    device_id = file['Device ID'][0]
    average_spl_value = round(file['Pressure'].mean(), 2)

    start_time = datetime.strptime(file['Timestamp'][0], datetime_format)
    end_time = datetime.strptime(file['Timestamp'][file['Timestamp'].count() - 1], datetime_format)

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
        moment = datetime.strptime(file['Timestamp'][i], datetime_format)
        spl_value = float(file['Pressure'][i])
        public_multiple_detail = PublicMultipleDetail(device_id=device_id, latitude=latitudes[i],
                                                      longitude=longitudes[i],
                                                      spl_value=spl_value, measured_at=moment,
                                                      measurement_id_id=measurement_id, user_name=username)

        public_multiple_detail.save()


def divide_by_time(file):
    start = 0
    end = 0

    ranges = []

    if datetime.strptime(str(file['Timestamp'][start][11:]), time_format) >= datetime.strptime('00:00:00', time_format):
        for i in range(start, len(file)):
            if datetime.strptime(str(file['Timestamp'][i][11:]), time_format) > datetime.strptime('05:00:00',
                                                                                                  time_format):
                end = i
                ranges.append([start, end])
                start = i
                break
            if i == len(file) - 1:
                end = i
                ranges.append([start, end])
                start = i
    else:
        ranges.append([0, 0])

    if start < len(file) - 1:
        if datetime.strptime(str(file['Timestamp'][start][11:]), time_format) >= datetime.strptime('05:00:00',
                                                                                                   time_format):
            for i in range(start, len(file)):
                if datetime.strptime(str(file['Timestamp'][i][11:]), time_format) > datetime.strptime('10:00:00',
                                                                                                      time_format):
                    ranges.append([start, end])
                    start = i
                    break

                if i == len(file) - 1:
                    end = i
                    ranges.append([start, end])
                    start = i
    else:
        ranges.append([0, 0])

    if start < len(file) - 1:
        if datetime.strptime(str(file['Timestamp'][start][11:]), time_format) >= datetime.strptime('10:00:00',
                                                                                                   time_format):
            for i in range(start, len(file)):
                if datetime.strptime(str(file['Timestamp'][i][11:]), time_format) > datetime.strptime('15:00:00',
                                                                                                      time_format):
                    ranges.append([start, end])
                    start = i
                    break

                if i == len(file) - 1:
                    end = i
                    ranges.append([start, end])
                    start = i
    else:
        ranges.append([0, 0])

    if start < len(file) - 1:
        if datetime.strptime(str(file['Timestamp'][start][11:]), time_format) >= datetime.strptime('15:00:00',
                                                                                                   time_format):
            for i in range(start, len(file)):
                if datetime.strptime(str(file['Timestamp'][i][11:]), time_format) > datetime.strptime('20:00:00',
                                                                                                      time_format):
                    ranges.append([start, end])
                    start = i
                    break

                if i == len(file) - 1:
                    end = i
                    ranges.append([start, end])
                    start = i
    else:
        ranges.append([0, 0])

    if start < len(file) - 1:
        if datetime.strptime(str(file['Timestamp'][start][11:]), time_format) >= datetime.strptime('20:00:00',
                                                                                                   time_format):
            for i in range(start, len(file)):
                if datetime.strptime(str(file['Timestamp'][i][11:]), time_format) > datetime.strptime('24:00:00',
                                                                           time_format):
                    ranges.append([start, end])
                    # start = i
                    break

                if i == len(file) - 1:
                    end = i
                    ranges.append([start, end])
                    start = i
    else:
        ranges.append([0, 0])

    print(ranges)

    return ranges


# TODO: fix the NaN value