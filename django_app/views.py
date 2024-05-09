from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import time

class DjangoTest(APIView):
    def __init__(self):
        pass

    def get(self,request):
        return JsonResponse({"output":f"The Django Application ran on {time.asctime()}"})

