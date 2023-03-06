from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


@admin.register(Asset)
class AssetAdmin(ImportExportModelAdmin):
    # ordering = ['-id']
    list_display = ('name', 'serial_number',
                    'purchase_date', 'status', 'img_preview')
    readonly_fields = ['img_preview']
    list_filter = ('status', 'purchase_date')
    search_fields = ('name', 'serial_number')
