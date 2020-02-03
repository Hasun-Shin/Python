from django.db import models


class Question(models.Model):
 question_text = models.CharField(max_length=200)
 pub_date = models.DateTimeField('date published')
 def __str__(self):
    return self.question_text

class Choice(models.Model):
 question = models.ForeignKey(Question, on_delete=models.CASCADE)
 choice_text = models.CharField(max_length=200)
 votes = models.IntegerField(default=0)
 def __str__(self):
    return str(self.question) + self.choice_text + str(self.votes)


class User(models.Model):
   user_name = models.CharField(max_length=20)
   is_superuser = models.BooleanField(default=False)
   def __str__(self):
      return self.user_name



class Album(models.Model):
   name = models.CharField(max_length=50)
   description = models.CharField(
     'One Line Description', max_length=100, null=True)
   owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
   def __str__(self):
      return self.name + '[' + self.owner.user_name + ']'


class Publication(models.Model):
   title = models.CharField(max_length=30)
   albums = models.ManyToManyField(Album)
   def __str__(self):
      return self.title



