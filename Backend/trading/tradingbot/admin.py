from django.contrib import admin
from .models import CSVFile
# Register your models here.
@admin.register(CSVFile)
class CSVFileAdmin(admin.ModelAdmin):
    list_display = ('file_name','file_path')