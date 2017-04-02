from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import DocumentForm_Single, DocumentForm_Multiple
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def model_form_single(request):
    if request.method == 'POST':
        if request.FILES['single']:
            print("this" + '-' * 20)
            form = DocumentForm_Single(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'noisesearch/test.html', {'form': form})
            else:
                print(form.errors)
                return render(request, 'noisesearch/test.html', {'form': form})


    else:
        form_single = DocumentForm_Single

        return render(request, 'noisesearch/test.html', {'form_single': form_single, })

@csrf_exempt
def model_form_multiple(request):
    if request.method == 'POST':
        if request.FILES['multiple']:
            form = DocumentForm_Multiple(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'noisesearch/test.html', {'form': form})
    else:
        form_multiple = DocumentForm_Multiple
        return render(request, 'noisesearch/test.html', {'form_multiple': form_multiple})