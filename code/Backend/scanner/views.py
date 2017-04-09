from django.http import HttpResponse
from .models import Data,DataTemp
from django.views.decorators.csrf import csrf_exempt
import datetime
from scanner.API import connection_scanning,ApiIpPlot,ApiPortPlot,connection2,TimeFetch,Bandwidth
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer,DataTempSerializer
from django.shortcuts import render
import time
import json

def home(request):
    return HttpResponse("<h1>abc</h1>")


def scan(request):
    connection_scanning.main()

def welcome(request):
    return render(request,'linking/welcome.html')


def displayip(request):
    ApiIpPlot.plotting()
    return HttpResponse('200')


def displayport(request):
    ApiPortPlot.plotting()
    return HttpResponse('200')

class FetchList(APIView):
    def get(self, request,format=None):
        data = connection2.main()
        print(data)
        #     # DataTemp.save()
        #     # serializer = DataTempSerializer(data, many=True)
        return HttpResponse(data)

    def post(self, request,format=None):
        data = connection2.main()
        print(data)
        #     # DataTemp.save()
        #     # serializer = DataTempSerializer(data, many=True)
        return HttpResponse(data)

class FetchTime(APIView):
        def post(self, request,format=None):
            Time1 = str(request.data.getlist('Time1')[0])
            Time2 = str(request.data.getlist('Time2')[0])
            t1 = Time1.split(':')
            t2 = Time2.split(':')
            print(t1[1])
            a = DataTemp.objects.filter(Time__gte=datetime.time(int(t1[0]), int(t1[1]), int(t1[2])),
                                    Time__lte=datetime.time(int(t2[0]), int(t2[1]), int(t2[2])))
            serializer = DataTempSerializer(a, many=True)

            return Response(serializer.data)

class FetchFrequency(APIView):
    def post(self, request,format=None):
        data = TimeFetch.calc_ul_dl()
        # print(data)
        #     # DataTemp.save()
        #     # serializer = DataTempSerializer(data, many=True)
        return HttpResponse(data)

class FetchBandwidth(APIView):
    def post(self, request,format=None):
        data = Bandwidth.main()
        # print(data)
        #     # DataTemp.save()
        #     # serializer = DataTempSerializer(data, many=True)
        return HttpResponse(data)
class FetchLog(APIView):
    def post(self, request,format=None):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)
