from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

import numpy as np
import functools

from . import plots
from . import finite_difference
from . import galerkin
from . import resolucion_analitica
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
    source = int(request.GET.get('source'))  * (1000)
    method = request.GET.get('method')
    method2 = request.GET.get('method2')
    compare = request.GET.get('compare')

    print(compare)
    print(method)
    print(method2)
    
    if compare == "true":
        print("COMPARACION")
        methods = {"method": method, "method2": method2}
        error_matrix = error.get_error_matrix(size, temperatures, source, methods)
        #print('-------------------------------------------')
        #print('error')
        #print(error_matrix)
        #print('-------------------------------------------')
        file_url = plots.create_plot(error_matrix)
    
        context =  {
            'fileUrl' : file_url
        }

    elif compare == "false":
        
        print(method)
        if method == 'diferencias_finitas':
            results = finite_difference.diferencias_finitas(temperatures, source, size)
            print('-------------------------------------------')
            print('diferencias_finitas')
            print(results)
            print(np.amax(results))
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
            print(np.amax(results))
            print('-------------------------------------------')
            file_url = plots.create_plot(results)

            context =  {
            'fileUrl' : file_url
            }

        elif method == 'analitica':
            results = resolucion_analitica.resolucion_analitica(size, temperatures, source)
            print('-------------------------------------------')
            print('analitica')
            print(results)
            print(np.amax(results))
            print('-------------------------------------------')
            file_url = plots.create_plot(results)
        
            context =  {
                'fileUrl' : file_url
            }
            
    return JsonResponse(context)
''' 

    temperatures = {"top": 0, "right": 0, "bottom": 0, "left": 0}

    for n in range (5, 50, 5):
        result1 = np.amax(finite_difference.diferencias_finitas(temperatures, 1000, n))
        result2 = np.amax(galerkin.galerkin(n, temperatures, 1000))
        result3 = np.amax(resolucion_analitica.resolucion_analitica(n, temperatures, 1000))
        print(str(n) + ": " + str(result1) + " | " +  str(result2) + " | " + str(result3))
'''    

