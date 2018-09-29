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
    # Se multiplica a la fuente por 10 a la 6 t se divide por k que vale 1000
    source = int(request.GET.get('source'))  * (1000000) / 1000
    method = request.GET.get('method')
    method2 = request.GET.get('method2')
    compare = request.GET.get('compare')

    print(size)
    print(temperatures)
    print(source)
    print(compare)
    print(method)
    print(method2)
    
    if compare == "true":
        print("COMPARACION")
        methods = {"method": method, "method2": method2}
        error_matrix = error.get_error_matrix(size, temperatures, source, methods)
        file_url = plots.create_plot(error_matrix)
    
        context =  {
            'fileUrl' : file_url
        }

    elif compare == "false":
        
        print(method)
        if method == 'diferencias_finitas':
            results = finite_difference.diferencias_finitas(size, temperatures, source)
            print('-------------------------------------------')
            print('diferencias_finitas')
            print(results)
            print(np.amax(results))
            print('-------------------------------------------')
            print("shutil")
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
            print(plots.create_plot())
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



