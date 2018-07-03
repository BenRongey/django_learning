from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def index(request):
    # print request.GET('polls', '')
    print(request.path)
    print(request.META['HTTP_HOST'])
    print(HttpRequest.get_full_path)
    if request.method == 'GET':
        return HttpResponse("Hello World")
    elif request.method == 'POST':
        return HttpResponse("YO WHAT UP")
    # # capturing postman request url from incoming
    
    # print(request.GET)
    # return HttpResponse("Hello World.  You are at the polls index.")
