from django.contrib import admin
from .models import W_Book, D_Book

# Register your models here.

class W_BookAdmin(admin.ModelAdmin):
    list_display=['MachineId','UserId','ValidTime','EndTime',]

class D_BookAdmin(admin.ModelAdmin):
    list_display=['MachineId','UserId','ValidTime','EndTime',]    

admin.site.register(W_Book,W_BookAdmin)
admin.site.register(D_Book,D_BookAdmin)