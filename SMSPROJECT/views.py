from django.shortcuts import render
from django.http import HttpResponse

def name(request):
    return HttpResponse("Hello, This Is New Web Page")