from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=256)
    principal=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    def __str__(self):
        return self.name
    #used for entering name to model through webpage
    #This will redirect to http://127.0.0.1:8000/basic_app/6/ school detail page
    def get_absolute_url(self):
        return reverse("basic_app_1:detail", kwargs={'pk':self.pk})

class Student(models.Model):
    name=models.CharField(max_length=256)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name
