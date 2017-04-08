from django.shortcuts import render, get_object_or_404
from .forms import DocumentForm_Single, DocumentForm_Multiple
from django.views.decorators.csrf import csrf_exempt
from .handleUploadedFile import handle_uploaded_file
from .models import Sum_measurement_single
from django.core import serializers
import json
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    objects = Sum_measurement_single.objects.all()
    json_data = serializers.serialize("json", objects)

    tobjects = json.loads(json_data)
    print('-' * 50)
    print(tobjects)
    print(len(tobjects))
    k = 0
    cells = []

    del tobjects[0]
    print('-' * 50)
    print(len(tobjects))

    print(tobjects[0]['fields']['latitude'])

    while(len(tobjects) != 0):
        cell = []
        x0 = tobjects[0]['fields']['latitude']
        y0 = tobjects[0]['fields']['longitude']
        del tobjects[0]

        for object in tobjects:
            x1 = object['fields']['latitude']
            y1 = object['fields']['longitude']
            if  pow((x1 - x0), 2) + pow((y1 - y0), 2) < 10:
                cell.append(object)
                del object
                
        cells.append(cell)
    print('-' * 50)
    print(len(cells))

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


def test_ajax(request):
    print(request)
    if  request.POST:
        print(request.POST)
    return HttpResponse('success')