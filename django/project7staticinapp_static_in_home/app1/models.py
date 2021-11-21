from django.db import models
from django.db.models.fields import CharField

class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=100,null=False,default="null")
    stuemail=models.EmailField(max_length=100)
    stupass=models.CharField(max_length=100)