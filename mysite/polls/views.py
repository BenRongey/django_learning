from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # capturing postman request url from incoming
    return HttpResponse("Hello World.  You are at the polls index.")