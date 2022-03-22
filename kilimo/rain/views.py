from rest_framework import viewsets, mixins, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .serializers import GroundSerializer, RainSerializer, GroundAvgRainSerializer, GroundRainSerializer, GroundSumRainSerializer
from .models import Ground, Rain
from datetime import datetime, timedelta
from django.db.models import Avg, Sum

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


class RainViewSet(viewsets.ModelViewSet):
    queryset = Rain.objects.all()
    serializer_class = RainSerializer


class GroundViewSet(viewsets.ModelViewSet):
    queryset = Ground.objects.all()
    serializer_class = GroundSerializer

    @action(detail=False, methods=['get'])
    def avg_rains(self, request):

        logger.debug('getting N param')
        n_days = request.query_params.get('N', '7')

        logger.debug('validating {}'.format(n_days))
        if not (n_days.isdigit()):
            n_days = 7
        elif (int(n_days) > 7):
            n_days = 7
        else:
            n_days = int(n_days)

        logger.debug('calculating date from')
        date_start = datetime.today() - timedelta(days=n_days)

        logger.debug('filtering queryset, and set average')
        queryset = self.get_queryset().filter(
            rain__rain_date__gte=date_start).annotate(average=Avg('rain__rainfall'))

        serializer = GroundAvgRainSerializer(queryset, many=True)

        logger.debug('return response')
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def sum_rains(self, request):

        logger.debug('getting N param')
        mm = request.query_params.get('N', '0')

        logger.debug('validating {}'.format(mm))
        if (mm.isdigit()):
            mm = int(mm)
        elif (mm.isnumber()):
            mm = float(mm)
        else:

            logger.error('N is not a number')
            raise serializers.ValidationError('N should be a number')

        logger.debug('filtering queryset, and set average')
        queryset = self.get_queryset().annotate(
            sum=Sum('rain__rainfall')).filter(sum__gte=mm)

        serializer = GroundSumRainSerializer(queryset, many=True)

        logger.debug('return response')
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def rains(self, request, pk=None):
        ground = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = GroundRainSerializer(ground)
        return Response(serializer.data)
