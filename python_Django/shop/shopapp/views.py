from django.shortcuts import render
from django.http import HttpResponse
from shopapp.models import Shop

def shop(request):
    shops = Shop.objects.all() #모든 데이터 가져오기
    

        

    return render(request, 'shopapp/shop.html',{'list':shops})