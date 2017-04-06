from django.shortcuts import render
from .forms import DocumentForm_Single, DocumentForm_Multiple
from django.views.decorators.csrf import csrf_exempt

from .HandleUploadedFile import handle_uploaded_file

# Create your views here.

def home_page(request):
    return render(request, 'noisesearch/home.html', {})

@csrf_exempt
def model_form_single(request):
    if request.method == 'POST':
        # if request.FILES["single"]:
        form_single = DocumentForm_Single(request.POST, request.FILES)
        if form_single.is_valid():
            # handle_uploaded_file(request.FILES['single'])
            file = form_single.save()
            file_name = file.single
            handle_uploaded_file(str(file_name))
            return render(request, 'noisesearch/form_single.html', {'form_single': form_single})
    else:
        form_single = DocumentForm_Single()
        return render(request, 'noisesearch/form_single.html', {'form_single': form_single, })
