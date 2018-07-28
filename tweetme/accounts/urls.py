from django.conf.urls import url,include

from django.views.generic.base import RedirectView

from .views import (
    UserDetailView
    )

urlpatterns = [
    
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /tweet/1/

]
