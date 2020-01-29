

from django.urls import path
from . import views #자기와 같은 경로에 있기 때문. 

urlpatterns = [
 path('main/', views.main, name='main'),
]

