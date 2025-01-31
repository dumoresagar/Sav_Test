from rest_framework import serializers
from .models import ScheduledAPICall

class APICallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledAPICall
        fields = '__all__'
