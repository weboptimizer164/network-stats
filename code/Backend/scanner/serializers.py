from rest_framework import serializers
from .models import Data,DataTemp

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'

class DataTempSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataTemp
        fields = ('Time','Date')