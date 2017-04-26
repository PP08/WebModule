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


def group_the_points(tobjects):
    data = []
    list_row = []
    # print('received object' + str(tobjects))

    while len(tobjects) > 0:
        row = []
        remove_id = []
        x0 = tobjects[0].latitude
        y0 = tobjects[0].longitude
        row.append(tobjects[0])

        # print('list_row ', row)
        del tobjects[0]

        if len(tobjects) > 0:
            for i in range(0, len(tobjects)):
                x1 = tobjects[i].latitude
                y1 = tobjects[i].longitude

                if haversine(x0, y0, x1, y1) < 30:
                    row.append(tobjects[i])
                    remove_id.append(i)

            if len(remove_id) > 0:
                tobjects = detele_element(tobjects, remove_id)
        list_row.append(row)

    if len(list_row) > 0:
        for r in list_row:
            ids = []
            sum_spl = sum_latitude = sum_longitude = 0
            for element in r:
                ids.append(element.id)
                sum_spl = sum_spl + element.average_spl
                sum_latitude = sum_latitude + element.latitude
                sum_longitude = sum_longitude + element.longitude

            average_spl_value = round(sum_spl / len(r), 2)
            average_latitude = sum_latitude / len(r)
            average_longitude = sum_longitude / len(r)
            data.append({'ids': ids, 'average_spl': average_spl_value, 'latitude': average_latitude,
                         'longitude': average_longitude})
    return data

def cal_distance(points):
    """"""
    distance = 0
    for i in range(len(points) - 1):
        distance = distance + haversine(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])
    return round(distance, 2)