from rest_framework import serializers
from djapp import models


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = '__all__'
