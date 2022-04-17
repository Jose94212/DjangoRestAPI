
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    html = '''<html><body>WELCOME</body></html>
            <html><body><br>HOME</body></html>''' 
    return HttpResponse(html)