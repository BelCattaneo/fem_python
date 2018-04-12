import numpy as np

from . import finite_difference
from . import galerkin
from . import resolucion_analitica


def get_error_matrix(size, temperatures, source, methods):
    
    method_1_result = finite_difference.diferencias_finitas(temperatures, source, size)
    method_2_result = galerkin.galerkin(size, temperatures, source)
    

    diff = np.subtract(method_1_result, method_2_result)
    print(diff)

    error_matrix = np.zeros((size, size), dtype=np.int)

    for y in range(0, size):
        for x in range(0, size):
            error_matrix[x,y] += (np.absolute(diff[x,y]) / method_2_result[x,y]) * 100

    return error_matrix

def get_results(size, temperatures, source, method):

    if method == 'diferencias_finitas':
        results = finite_difference.diferencias_finitas(temperatures, source, size)
            
    elif method == 'galerkin':
        results = galerkin.galerkin(size, temperatures, source)
            
    elif method == 'analitica':
        results = resolucion_analitica.resolucion_analitica(size, temperatures, source)
        
    return results