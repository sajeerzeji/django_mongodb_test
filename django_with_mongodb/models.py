from django.db import models


# Create your models here.

class PingPongModel(models.Model):
    pong = models.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)