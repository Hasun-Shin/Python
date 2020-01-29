from django.db import models

from django.db import models
class Curriculum(models.Model):
 name = models.CharField(max_length=255)

 def __str__(self):
     return str(self.id) + '번 / ' + self.name 
