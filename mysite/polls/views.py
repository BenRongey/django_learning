from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    p_id = request.GET['pid']
    m_id = request.GET['mid']
    monitorId = p_id
    enqId = m_id
    # new_url_response = (request.META['HTTP_HOST'] + request.path +'?first_name=' + request.GET['name'])
    # return HttpResponse(new_url_response)
    return redirect(request.META['HTTP_HOST'])


    
    
    # print(HttpRequest.get_full_path)
    # if request.method == 'GET':
    #     return HttpResponse("Hello World")
    # elif request.method == 'POST':
    #     return HttpResponse("YO WHAT UP")
    # # # capturing postman request url from incoming
    
    # # print(request.GET)
    # # return HttpResponse("Hello World.  You are at the polls index.")
