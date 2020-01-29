from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Curriculum

# Create your views here.

def index1(request):
    return HttpResponse('<h1>Index1</h1>')

def index2(request):
    return HttpResponse('<h1>Hi</h1>')

def main(request):
    list = Curriculum.objects.all() #모든 데이터 가져오기
    html = ''
    for cur in list:
        html += cur.name + '<br>'

    return render(request, 'firstapp/main.html',{'list':list}) 