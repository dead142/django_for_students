from django.shortcuts import render

# Create your views here.

def index(request):
    return  render(request, 'second/home.html')

def contact(request):
    return  render(request, 'second/basic.html',{'values': ["sfsdf" , "sfddsf"]})