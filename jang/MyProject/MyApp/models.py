from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class Student(models.Model):
#           first_name = models.CharField(max_length=50)
#           last_name = models.CharField(max_length=50)
#           score = models.IntegerField()
#           def __str__(self):
#                   return self.first_name + " " + self.last_name
# class Customer(models.Model):
#           name = models.CharField(max_length=50)
#           email = models.EmailField(max_length=50)
#           password = models.CharField(max_length=100)
#           def __str__(self):
#                   return self.name
# class Signup(models.Model):
#           username = models.CharField(max_length=50)
#           email = models.EmailField(max_length=50)
#           password = models.CharField(max_length=100)
#           def __str__(self):
#                   return self.username
# class Author(models.Model):
#           name = models.CharField(max_length=50)
#           email = models.EmailField()
#           description = models.TextField()
#           def __str__(self):
#                   return self.name
# class Book(models.Model):
#           title = models.CharField(max_length=50)
#           author = models.ForeignKey(Author, on_delete = models.CASCADE)
#           published_date = models.DateField()
#           def __str__(self):
#                   return self.title
# class Blogspot(models.Model):
#         post_id = models.AutoField(primary_key=True)
#         title = models.CharField(max_length=30)
#         post = models.TextField()
#         thumbnail = models.ImageField(upload_to='iamges/', default='')
#         def __str__(self):
#                 return self.title
class Customer(models.Model):
          name = models.CharField(max_length=50)
          email = models.EmailField(max_length=50)
          password = models.CharField(max_length=100)
          def __str__(self):
                  return self.name

class CustomUser(models.Model):
    security_question_1 = models.CharField(max_length=100)
    security_answer_1 = models.CharField(max_length=100)
    security_question_2 = models.CharField(max_length=100)
    security_answer_2 = models.CharField(max_length=100)
    security_question_3 = models.CharField(max_length=100)
    security_answer_3 = models.CharField(max_length=100)
