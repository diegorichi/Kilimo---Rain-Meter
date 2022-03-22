from rest_framework import serializers
from django.db.models import Avg
from .models import Ground, Rain
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rain
        fields = ('id', 'rain_date', 'rainfall','ground')


class GroundSerializer(serializers.ModelSerializer):
    rain_set = RainSerializer(many=True, read_only=True)

    class Meta:
        model = Ground
        fields = ('id', 'name', 'lat', 'lon', 'hectare', 'rain_set')

class GroundAvgRainSerializer(serializers.ModelSerializer):
    average = serializers.SerializerMethodField()

    class Meta:
        model = Ground
        fields = ('id', 'name','average')

    def get_average(self, obj):
        logger.info('Returning rain average')
        return obj.average

class GroundSumRainSerializer(serializers.ModelSerializer):
    sum = serializers.SerializerMethodField()

    class Meta:
        model = Ground
        fields = ('id', 'name','sum')

    def get_sum(self, obj):
        logger.info('Returning rain sum')
        return obj.sum


class GroundRainSerializer(serializers.ModelSerializer):

    rain_set = RainSerializer(many=True)

    class Meta:
        model = Ground
        fields = ('id', 'name','rain_set')

