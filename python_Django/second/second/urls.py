
from django.contrib import admin
from django.urls import path, include
from secondapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('second/', include('secondapp.urls')), #second 주소를 거쳐야만 갈 수 있음.
    
]
