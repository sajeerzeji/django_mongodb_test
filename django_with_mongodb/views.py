from django.shortcuts import render


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from django_with_mongodb.models import PingPongModel
from django_with_mongodb.serializers import PingPongSerializer


class PingPongViews(APIView):

    def get(self, request):
        pingPong = PingPongModel()
        pingPong.pong = 'pong'
        serializer = PingPongSerializer(pingPong, many=False)
        return Response(serializer.data)