from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class UserDisplaySerializer(serializers.ModelSerializer):
    follow_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields=[
            'username','first_name','last_name','follow_count'
        ]
    def get_follow_count(self,obj):
            return 0
