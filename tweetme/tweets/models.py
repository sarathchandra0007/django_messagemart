from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import restrictmodel
from django.urls import reverse
from django.utils.timesince import timesince
# from django.contrib.auth import get_user_model
# # Create your models here.
# 
# User = get_user_model()


class Tweet(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    content     = models.CharField(max_length=140,validators=[restrictmodel])
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('tweets_app:detail', kwargs={"pk":self.pk})
    # Models one way of validation which can be declared in class
    def clean(self,*args,**kwargs):
        content=self.content
        if content=='sarath':
            raise ValidationError("Dont enter ur name")
        return super(Tweet,self).clean(*args,**kwargs)


    class Meta:
        ordering = ['-timestamp','content']
