from rest_framework import serializers
from .models import PingPongModel

class PingPongSerializer(serializers.ModelSerializer):

    class Meta:
        model = PingPongModel
        fields = '__all__'