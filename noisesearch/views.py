from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from .models import Sum_measurement_single, PrivateSingleAverage, PublicSingleAverage, PublicSingleDetail
from django.core import serializers
import json
from django.http import HttpResponse
from . import coordinates_helper
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_page(request):
    global average_longitude, average_latitude, average_spl_value, ids

    objects = serializers.serialize("json", PublicSingleAverage.objects.all())

    tobjects = json.loads(objects)

    data = coordinates_helper.group_the_points(tobjects)
    # print(data)
    json_data = json.dumps(data)

    # print(json_data)
    return render(request, 'noisesearch/home.html', {'points': json_data})


# @csrf_exempt
# def model_form_single(request):
#     if request.method == 'POST':
#         form_single = DocumentForm_Single(request.POST, request.FILES)
#         if form_single.is_valid():
#             file = form_single.save()
#             file_name = file.single
#             print('filename: ', file_name)
#             handle_uploaded_file(str(file_name))
#             return render(request, 'noisesearch/form_single.html', {'form_single': form_single})
#     else:
#         form_single = DocumentForm_Single()
#         return render(request, 'noisesearch/form_single.html', {'form_single': form_single, })


def get_details(request):
    indices = request.GET.getlist('ids[]')
    data = []
    for id in indices:
        data.append(serializers.serialize('json', PublicSingleAverage.objects.filter(id=int(id))))

    returnString = ""
    for element in data:
        returnString = returnString + element + ', '

    returnString = returnString[:-2]
    return HttpResponse(
        returnString,
        content_type="application/text")


@csrf_exempt
def data_filter(request):
    # max_duration, min_spl, max_spl, max_date, min_date, objects = None
    min_duration = None
    max_duration = None
    min_spl = None
    max_spl = None
    min_date = None
    max_date = None
    global objects

    filters = request.POST.get('filters')
    filters = json.loads(filters)

    # print(filters)

    for f in filters:
        if f['name'] == 'min_duration':
            min_duration = f['value']
        elif f['name'] == 'max_duration':
            max_duration = f['value']
        elif f['name'] == 'min_spl':
            min_spl = f['value']
        elif f['name'] == 'max_spl':
            max_spl = f['value']
        elif f['name'] == 'min_date':
            min_date = f['value']
        elif f['name'] == 'max_date':
            max_date = f['value']

    objects = Sum_measurement_single.objects.all()

    if min_duration != None:
        min_duration = timedelta(minutes=int(min_duration))
        max_duration = timedelta(minutes=int(max_duration))
        objects = objects.filter(measurement_duration__gte=min_duration).filter(measurement_duration__lte=max_duration)

    if (min_spl != None):
        objects = objects.filter(average_spl_value__gte=int(min_spl)).filter(average_spl_value__lte=int(max_spl))

    if (min_date != None):
        min_date = coordinates_helper.convert_date_time(min_date)
        max_date = coordinates_helper.convert_date_time(max_date)

        objects = objects.filter(start_time__gte=min_date).filter(start_time__lte=max_date)

    context = {"message": "No objects match your filter(s)"}

    if (len(objects) > 0):
        objects = serializers.serialize('json', objects)
        tobjects = json.loads(objects)
        data = coordinates_helper.group_the_points(tobjects)
        return_data = json.dumps(data)
    else:
        return_data = json.dumps(context)

    # todo: return data when get null objects

    return HttpResponse(
        return_data,
        content_type="application/json"
    )



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'noisesearch/signup.html', {'form': form})


@login_required
def data_manager(request):
    current_user = request.user

    # print(current_user.id)

    private_data = PrivateSingleAverage.objects.filter(user_name=current_user)
    public_data = PublicSingleAverage.objects.filter(user_name=current_user)


    return render(request, 'noisesearch/user_data.html', {'private_data': private_data, 'public_data': public_data})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('disabled account')

            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'noisesearch/login.html', {'form': form})



def get_detail_pbs(request, pk):
    # measurement = get_object_or_404(PublicSingleDetail, measurement_id=pk)

    measurement = PublicSingleDetail.objects.filter(measurement_id=pk).order_by('measured_at')
    print(measurement)

    return render(request, 'noisesearch/details_data.html', {'measurement': measurement})

