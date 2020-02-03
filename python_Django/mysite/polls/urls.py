from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('free/', views.free, name='free'),
 path('insert/', views.insert, name='insert'),
 path('<int:question_id>/', views.detail, name='detail'),
 path('<int:question_id>/new_choice', views.new_choice, name='new_choice'),
 path('<int:question_id>/results', views.results, name='results'),
 path('<int:question_id>/vote', views.vote, name='vote'),
]
