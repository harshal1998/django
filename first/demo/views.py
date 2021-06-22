from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def a(request):
    msg = "Hi Harshal"
    return HttpResponse(msg)
