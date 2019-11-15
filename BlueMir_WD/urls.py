from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('account/',include('account.urls')),
    path('reserve/',include('reserve.urls')),
]
