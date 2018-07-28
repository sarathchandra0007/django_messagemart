from rest_framework import generics
from .serializers import TweeetModelSerializer
from tweets.models import Tweet

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweeetModelSerializer
    def get_queryset(self):
        return Tweet.objects.all()
