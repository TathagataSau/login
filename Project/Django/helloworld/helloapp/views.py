from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse(f"Hello Tathagata = {2+23}")


