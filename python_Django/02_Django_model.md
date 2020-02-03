모델.



모델은 app/models.py 내 파이썬 클래스로 표현



setting.py

```python
INSTALLED_APPS = [
 '추가할 APP',
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
]
```



관리자 사이트

app/admin.py



```python
from django.contrib import admin
from .models import 모델클래스
admin.site.register(models.Model):모델클래스)
```



Field Type

<img src="C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200203104028502.png" alt="image-20200203104028502" style="zoom:67%;" />

 Field Option



```python
class 모델클래스(models.Model):models.Model):
 속성1 = models.CharField(models.Model):max_length=30, null=True)
 속성2 = models.IntegerField(models.Model):default=0)
```



<img src="C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200203104309470.png" alt="image-20200203104309470" style="zoom:67%;" />



 Manager 속성

ex) 모든 데이터 조회 → 모델클래스.objects.all(models.Model):)

```python
from django.db import models
# 매니저 정의
class SecondManager(models.Model):models.Manager):
 def get_queryset(models.Model):self):
 return super(models.Model):SecondManager, self).get_queryset(models.Model):).filter(models.Model):name__contains='kim')

class Curriculum(models.Model):models.Model):
 name = models.CharField(models.Model):max_length=255)
 objects = models.Manager(models.Model):)
 second_objects = SecondManager(models.Model):)

 def __str__(models.Model):self):
 return self.name
```



장고 쉘을 이용한 모델 함수 테스트 - python manage.py shell

\- 데이터 조회 : 모델클래스.objects.get(models.Model):속성=검색어)

\- 데이터 조회 : 모델클래스.objects.filter(models.Model):속성=검색어)

`Curriculum.objects.filter(name__contains='chain')` 

언더바 두줄 : chain 으로 끝나는 속성 가져옴. 

\- 데이터 제외 : 모델클래스.objects.exclude(models.Model):속성=검색어)

\- 데이터 개수 : 모델클래스.objects.count(models.Model):





모델 관계

3가지 관계

1:N, N:N, 1:1



1:1

OneToOneField

```python
class Restaurant(models.Model):models.Model):
 place = models.OneToOneField(models.Model):Place, on_delete=models.CASCADE)
 name = models.CharField(models.Model):max_length=50, default='DefRestName')
 serves_pizza = models.BooleanField(models.Model):default=False)
 def __str__(models.Model):self):
 return '%s the restaurant' % self.name
```



-------

뷰 템플릿



구현 2가지

- 함수 기반

- 클래스 기반 : 더 많이 쓰임. 
  - Class-based views/ Include App urls
  - app/views.py 내 파이썬 클래스로 표현. 