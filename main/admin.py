from django.contrib import admin
from .models import Washer,Dryer

class WasherAdmin(admin.ModelAdmin):
    list_display=['Place','Number']

class DryerAdmin(admin.ModelAdmin):
    list_display=['Place','Number']
   
admin.site.register(Washer,WasherAdmin)
admin.site.register(Dryer,DryerAdmin)
