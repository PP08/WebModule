from django.shortcuts import render, get_object_or_404
from .forms import DocumentForm_Single, DocumentForm_Multiple
from django.views.decorators.csrf import csrf_exempt
from .handleUploadedFile import handle_uploaded_file
from .models import Sum_measurement_single, Table_single
from django.core import serializers
import json
from django.http import JsonResponse, HttpResponse
from . import coordinates_helper

import itertools

# Create your views here.

def home_page(request):
    global average_longitude, average_latitude, average_spl_value, ids

    objects = serializers.serialize("json", Sum_measurement_single.objects.all())

    print(Sum_measurement_single.objects.all())
    print(objects)

    tobjects = json.loads(objects)

    data = []
    while(len(tobjects) > 0):

        list_row = []
        remove_id = []
        x0 = tobjects[0]['fields']['latitude']
        y0 = tobjects[0]['fields']['longitude']
        list_row.append(tobjects[0])
        del tobjects[0]

        if len(tobjects) > 0:
            for i in range(0, len(tobjects)):
                x1 = tobjects[i]['fields']['latitude']
                y1 = tobjects[i]['fields']['longitude']

                if coordinates_helper.haversine(x0, y0, x1, y1) < 30:
                    list_row.append(tobjects[i])
                    remove_id.append(i)

            if len(remove_id) > 0:
                tobjects = coordinates_helper.detele_element(tobjects, remove_id)

            ids = []
            sum_spl = sum_latitude = sum_longitude = 0

            for element in list_row:
                ids.append(element['pk'])
                sum_spl = sum_spl + element['fields']['average_spl_value']
                sum_latitude = sum_latitude + element['fields']['latitude']
                sum_longitude = sum_longitude + element['fields']['longitude']

            average_spl_value = round(sum_spl / len(list_row), 2)
            average_latitude = sum_latitude / len(list_row)
            average_longitude = sum_longitude / len(list_row)
            data.append({'ids': ids, 'average_spl_value': average_spl_value, 'latitude': average_latitude, 'longitude': average_longitude})


    # print(data)
    json_data = json.dumps(data)

    # print(json_data)
    return render(request, 'noisesearch/home.html', {'points': json_data})

@csrf_exempt
def model_form_single(request):
    if request.method == 'POST':
        form_single = DocumentForm_Single(request.POST, request.FILES)
        if form_single.is_valid():
            file = form_single.save()
            file_name = file.single
            handle_uploaded_file(str(file_name))
            return render(request, 'noisesearch/form_single.html', {'form_single': form_single})
    else:
        form_single = DocumentForm_Single()
        return render(request, 'noisesearch/form_single.html', {'form_single': form_single, })


def get_details(request):

    indices = request.GET.getlist('ids[]')
    data = []
    for id in indices:
        data.append(serializers.serialize('json', Sum_measurement_single.objects.filter(measurement_id=int(id))))

    returnString = ""
    for element in data:
        returnString = returnString + element + ', '


    returnString = returnString[:-2]
    return HttpResponse(
        returnString,
        content_type="application/text")