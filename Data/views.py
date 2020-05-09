from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Data.forms import ClassificationForm, UploadFileForm
import Data.Mining as Mining

def index(request):
    return render(request,'index.html')

def Classification(request):
    return render(request,'classification.html')

def KNN_Classification(request):
    return render(request,'KNN.html')

def KNN_Classify(request):
    response = HttpResponse(content_type='text/csv')
    FormData = ClassificationForm(request.POST,request.FILES)
    print("HEllO")
    if FormData.is_valid():
        print("HEllO")
        DF = Mining.KNN_Classification(FormData.Train_Data_File,
                                       FormData.Test_Data_File,
                                       FormData.Label_Name,
                                       FormData.K_Value)
        results = DF
        response['Content-Disposition'] = 'attachment; filename=filename.csv'
        results.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
    return response

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)