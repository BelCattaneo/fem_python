import numpy as np
import math

from . import finite_difference
from . import galerkin
from . import resolucion_analitica


def get_error_matrix(size, temperatures, source, methods):
    
    method_1_result = get_results(size, temperatures, source, methods["method"])
    method_2_result = get_results(size, temperatures, source, methods["method2"])
    
    diff = np.subtract(method_2_result, method_1_result)

    error_matrix_size = size-2
    error_matrix = np.zeros((error_matrix_size, error_matrix_size), dtype=np.int)
    
    results = []
    for y in range(0, error_matrix_size):
        for x in range(0, error_matrix_size):

            if method_2_result[x,y] != 0:
                error = (np.absolute(diff[x,y]) / method_2_result[x,y]) * 100
                error_matrix[x,y] += error
                results.append(error)
                
    error_average = np.sum(results)/(np.array(results)).size
    print("Size: " + str(size) + "Error Promedio: " + str(error_average))
    return error_matrix

def get_results(size, temperatures, source, method):

    if method == 'diferencias_finitas':
        results = finite_difference.diferencias_finitas(size, temperatures, source)
            
    elif method == 'galerkin':
        results = galerkin.galerkin(size, temperatures, source)
            
    elif method == 'analitica':
        results = resolucion_analitica.resolucion_analitica(size, temperatures, source)
        
    return results
