import numpy as np
import math

def calculo_sumatoria(x, y):
    sumatoria = 0
    pi = math.pi
    for n in range (0, 100):
        X=2*x
        Y=2*y
        m = (2*n + 1)
        k = pi*m/2
        signo = math.pow((-1), n)
        numerador = (math.cosh(k*X)*math.cos(k*Y))
        denominador = math.pow(k, 3)*math.cosh(k)
        
        sumatoria += signo*numerador/denominador
        
    return sumatoria
    
def calculo_temperatura(size, temperature, source):
    results_matrix_size =  (size - 2)
    
    results_matrix = []
    
    step = 1 / results_matrix_size
    start = (- step * results_matrix_size) + step
    end = (step * results_matrix_size) - step
    print(start)
    print(end)
    print(step)
    for y in np.arange(start, end, step):
        row = []
        for x in np.arange(start, end, step):
            sumatoria = calculo_sumatoria(x, y)
            print(((1-math.pow(y/2, 2))/8 - 1/2*sumatoria)*source)
            result = ((1-math.pow(y/2, 2))/8 - 1/2*sumatoria)*source + temperature
            
            row.append(temperature)
        results_matrix.insert(0, row)
        
    print(results_matrix)
    results = np.array(results_matrix).flatten()
     
    return results
     
     
print(calculo_temperatura(5, 20, 4))