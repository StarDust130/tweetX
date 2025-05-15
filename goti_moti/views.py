from django.shortcuts import render

# Create your views here.

def hello_goti(request):
    return render(request , "index.html" )
