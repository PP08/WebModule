from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from .models import PrivateSingleAverage, PublicSingleAverage, PublicSingleDetail, \
    PrivateSingleDetail, PrivateMultipleAverage, PrivateMultipleDetail
from django.core import serializers
import json
from django.http import HttpResponse
from . import coordinates_helper
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.core.serializers.json import DjangoJSONEncoder
import ast


# Create your views here.

def home_page(request):
    # print(request.GET.get('values')[0])

    global average_longitude, average_latitude, average_spl_value, ids, objects, sp_objects

    sp_objects = []

    if request.GET.get('modelName') == None:
        # objects = serializers.serialize("json", PublicSingleAverage.objects.all())
        objects = PublicSingleAverage.objects.all()
    else:
        ids = request.GET.get('values')
        ids = ast.literal_eval(ids)
        model_name = request.GET.get('modelName')
        # sp_objects = []
        if model_name == 'privateSingle':
            if str(request.user) != PrivateSingleAverage.objects.get(pk=int(ids[0])).user_name:
                return render(request, 'noisesearch/home.html', {'point': None})
            else:
                for id in ids:
                    sp_objects.append(PrivateSingleAverage.objects.get(pk=int(id)))
        elif model_name == 'publicSingle':
            for id in ids:
                sp_objects.append(PublicSingleAverage.objects.get(pk=int(id)))

    temp = []

    if len(sp_objects) == 0:
        # tobjects = json.loads(objects)
        for ob in objects:
            temp.append(ob)
        tobjects = temp
    else:
        tobjects = sp_objects

    # tobjects = json.loads(objects)

    # print(tobjects[0].average_spl)

    data = coordinates_helper.group_the_points(tobjects)
    # print(data)
    json_data = json.dumps(data)

    # print(json_data)
    return render(request, 'noisesearch/home.html', {'points': json_data})


def get_details_pbs(request):
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

1

@login_required
def get_details_prs(request):
    indices = request.GET.getlist('ids[]')

    if str(request.user) != PrivateSingleAverage.objects.get(pk=int(indices[0])).user_name:
        return HttpResponse(
            "nothing",
            content_type="application/text"
        )
    else:
        data = []
        for id in indices:
            data.append(serializers.serialize('json', PrivateSingleAverage.objects.filter(id=int(id))))

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

    objects = PublicSingleAverage.objects.all()

    if min_duration != None:
        min_duration = timedelta(minutes=int(min_duration))
        max_duration = timedelta(minutes=int(max_duration))
        objects = objects.filter(duration__gte=min_duration).filter(duration__lte=max_duration)

    if (min_spl != None):
        objects = objects.filter(average_spl__gte=int(min_spl)).filter(average_spl__lte=int(max_spl))

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

    private_data_single = PrivateSingleAverage.objects.filter(user_name=current_user)
    public_data_single = PublicSingleAverage.objects.filter(user_name=current_user)

    return render(request, 'noisesearch/user_data.html',
                  {'private_data_single': private_data_single, 'public_data_single': public_data_single})


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

    measurements = PublicSingleDetail.objects.filter(measurement_id=pk).order_by('measured_at')

    print(measurements[0].measured_at)
    return render(request, 'noisesearch/details_data.html', {'measurements': measurements})


@login_required
def get_detail_prs(request, pk):
    measurements = PrivateSingleDetail.objects.filter(measurement_id=pk, user_name=str(request.user))
    return render(request, 'noisesearch/details_data.html', {'measurements': measurements})


@login_required
@csrf_exempt
def delete_selected_data(request):
    model_name = request.POST.get('modelName')
    ids = request.POST.getlist('ids[]')

    if model_name == 'privateSingle':
        for id in ids:
            PrivateSingleAverage.objects.filter(id=int(id), user_name=request.user).delete()

    elif model_name == 'publicSingle':
        for id in ids:
            PublicSingleAverage.objects.filter(id=int(id), user_name=request.user).delete()

    return_data = {'message': 'success'}
    return_data = json.dumps(return_data)

    return HttpResponse(
        return_data,
        content_type="application/json"
    )


@login_required
@csrf_exempt
def change_state_single(request):
    """"""
    global return_data
    model_name = request.POST.get('modelName')
    ids = request.POST.getlist('ids[]')

    new_ids = []
    return_objects = []

    if model_name == 'privateSingle':
        if PrivateSingleAverage.objects.get(id=int(ids[0])).user_name == str(request.user):
            for id in ids:
                prs_object = PrivateSingleAverage.objects.get(id=int(id))
                prsd_object = PrivateSingleDetail.objects.filter(measurement_id_id=int(id))

                pbs = PublicSingleAverage(device_id=prs_object.device_id, latitude=prs_object.latitude,
                                          longitude=prs_object.longitude,
                                          average_spl=prs_object.average_spl, duration=prs_object.duration,
                                          start_time=prs_object.start_time,
                                          end_time=prs_object.end_time, user_name=prs_object.user_name)
                pbs.save()

                new_ids.append(pbs.id)

                return_objects.append(serializers.serialize("json", PublicSingleAverage.objects.filter(id=pbs.id)))

                for ob in prsd_object:
                    pbsd = PublicSingleDetail(measurement_id_id=pbs.id, device_id=ob.device_id, latitude=ob.latitude,
                                              longitude=ob.longitude, spl_value=ob.spl_value,
                                              measured_at=ob.measured_at, user_name=ob.user_name)
                    pbsd.save()
                prs_object.delete()
                prsd_object.delete()

    elif model_name == 'publicSingle':
        """"""
        if PublicSingleAverage.objects.get(id=int(ids[0])).user_name == str(request.user):
            for id in ids:
                pbs_object = PublicSingleAverage.objects.get(id=int(id))
                pbsd_object = PublicSingleDetail.objects.filter(measurement_id_id=int(id))

                prs = PrivateSingleAverage(device_id=pbs_object.device_id, latitude=pbs_object.latitude,
                                           longitude=pbs_object.longitude,
                                           average_spl=pbs_object.average_spl, duration=pbs_object.duration,
                                           start_time=pbs_object.start_time,
                                           end_time=pbs_object.end_time, user_name=pbs_object.user_name)
                prs.save()

                new_ids.append(prs.id)

                return_objects.append(serializers.serialize("json", PrivateSingleAverage.objects.filter(id=prs.id)))

                for ob in pbsd_object:
                    prsd = PrivateSingleDetail(measurement_id_id=prs.id, device_id=ob.device_id, latitude=ob.latitude,
                                               longitude=ob.longitude, spl_value=ob.spl_value,
                                               measured_at=ob.measured_at, user_name=ob.user_name)
                    prsd.save()
                pbs_object.delete()
                pbsd_object.delete()
                # return_data = {'message': 'success', 'ids': new_ids, 'objects': return_objects}

    returnString = ""
    for element in return_objects:
        returnString = returnString + element + ', '

    returnString = returnString[:-2]
    return HttpResponse(
        returnString,
        content_type="application/text")


def renderGraphsPublic(request):
    spl_values = []
    timestamps = []

    objects = PublicSingleDetail.objects.filter(measurement_id=int(request.GET.get('id')))

    for ob in objects:
        spl_values.append(ob.spl_value)
        timestamps.append(ob.measured_at.astimezone())

    # print(timestamps[0])

    return_data = {'spl_values': spl_values, 'timestamps': timestamps}

    return_data = json.dumps(return_data, cls=DjangoJSONEncoder)

    # print(return_data)

    return HttpResponse(
        return_data,
        content_type='application/json'
    )


@login_required
def renderGraphsPrivate(request):
    spl_values = []
    timestamps = []

    objects = PrivateSingleDetail.objects.filter(measurement_id=int(request.GET.get('id')))

    for ob in objects:
        spl_values.append(ob.spl_value)
        timestamps.append(ob.measured_at.astimezone())

    # print(timestamps[0])

    return_data = {'spl_values': spl_values, 'timestamps': timestamps}

    return_data = json.dumps(return_data, cls=DjangoJSONEncoder)

    # print(return_data)

    return HttpResponse(
        return_data,
        content_type='application/json'
    )


def multiple_map(request):
    """"""
    objects = PrivateMultipleAverage.objects.all()
    return render(request, 'noisesearch/multiple.html', {'object': objects})

def test(request):
    """"""

    return render(request, 'noisesearch/test/test.html')
