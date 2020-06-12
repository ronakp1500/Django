from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"Bootapp/test.html")
def index1(request):
    return HttpResponse("Hello to Bootcamp1 url")
