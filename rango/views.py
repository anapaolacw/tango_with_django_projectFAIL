from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    #return render(request, 'rango/about.html')
    return HttpResponse('Rango says here is the about page.<br><a href=\'/rango/\'>Index</a>')
