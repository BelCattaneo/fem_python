from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
    return render_to_response('fem/index.html')

def result(request):
    size = request.GET['size']
    top = request.GET['top']
    right = request.GET['right']
    bottom = request.GET['bottom']
    left = request.GET['left']
    context =  {'data': 
        {
            'size' : size,
            'top' : top,
            'right' : right,
            'bottom' : bottom,
            'left' : left
        }
    }
    print(context)
    return render(request, 'fem/index.html', context)