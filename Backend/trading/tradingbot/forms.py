from django import forms
from .models import CSVFile

class CSVFileForm(forms.Form):
    csv_file = forms.ModelChoiceField(queryset=CSVFile.objects.all(), label="Select CSV File")
