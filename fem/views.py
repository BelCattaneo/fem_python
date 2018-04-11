from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

import numpy as np
import functools

from . import plots
from . import finite_difference
from . import galerkin
from . import error

def index(request):
    return render_to_response('fem/index.html')

def calculate_temperatures(request):
    size = int(request.GET.get('size'))
    temperatures = {
        'top' : int(request.GET.get('top')),
        'right' : int(request.GET.get('right')),
        'bottom' : int(request.GET.get('bottom')),
        'left' : int(request.GET.get('left')),
    }
    source = int(request.GET.get('source'))
    method = request.GET.get('method')

    print(method)
    if method == 'diferencias_finitas':
        results = finite_difference.diferencias_finitas(temperatures, source, size)
        print('-------------------------------------------')
        print('diferencias_finitas')
        print(results)
        print('-------------------------------------------')
        file_url = plots.create_plot(results)

        context =  {
        'fileUrl' : file_url
        }
        
    elif method == 'galerkin':
        results = galerkin.galerkin(size, temperatures, source)
        print('-------------------------------------------')
        print('galerkin')
        print(results)
        print('-------------------------------------------')
        file_url = plots.create_plot(results)

        context =  {
        'fileUrl' : file_url
        }

    elif method == 'error':
        error_matrix = error.get_error_matrix(size, temperatures, source)
        print('-------------------------------------------')
        print('error')
        print(error_matrix)
        print('-------------------------------------------')
        file_url = plots.create_plot(error_matrix)
    
        context =  {
            'fileUrl' : file_url
        }



    return JsonResponse(context)
