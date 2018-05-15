import numpy as np
import math

from . import finite_difference
from . import galerkin
from . import resolucion_analitica


def get_error_matrix(size, temperatures, source, methods):
    
    method_1_result = get_results(size, temperatures, source, methods["method"])
    method_2_result = get_results(size, temperatures, source, methods["method2"])
    #print(method_1_result)
    #print(method_2_result)
    
    diff = np.subtract(method_1_result, method_2_result)
    #print(diff)

    error_matrix = np.zeros((size, size), dtype=np.int)
    results = []
    print("lalala")
    for y in range(1, size-1):
        for x in range(1, size-1):

            if method_2_result[x,y] != 0:
                error = (np.absolute(diff[x,y]) / method_2_result[x,y]) * 100
                error_matrix[x,y] += error
                results.append(error)
                
    error_average = np.sum(results)/(np.array(results)).size
    print("Error Promedio: " + str(error_average))
    return error_matrix

def get_results(size, temperatures, source, method):

    if method == 'diferencias_finitas':
        results = finite_difference.diferencias_finitas(temperatures, source, size)
            
    elif method == 'galerkin':
        results = galerkin.galerkin(size, temperatures, source)
            
    elif method == 'analitica':
        results = resolucion_analitica.resolucion_analitica(size, temperatures, source)
        
    return results
