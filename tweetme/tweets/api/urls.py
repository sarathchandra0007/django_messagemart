from django.conf.urls import url
from .views import TweetListAPIView
from django.views.generic.base import RedirectView
urlpatterns=[
    url(r'^$',TweetListAPIView.as_view(),name='list'),

]
