
from django import forms

class ClassificationForm(forms.Form):
    Train_Data_File = forms.FileField()
    Test_Data_File = forms.FileField()
    K_Value = forms.IntegerField(label="Enter K Value")
    Label_Name = forms.CharField(label="Enter Label Name")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()