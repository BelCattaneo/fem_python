import numpy as np
import math
from scipy import integrate


def resolucion_analitica(size, temperatures, source):
    method_temperatures = get_temperatures_I(temperatures, size)
    method_source = get_temperatures_II(size, source)

    results = np.array(method_temperatures) + np.array(method_source)

    final_matrix = build_final_matrix(results)

    return final_matrix

def sumation(temperatures, x, y):
    pi = math.pi

    t1 = temperatures["top"]
    t2 = temperatures["right"]
    t3 = temperatures["bottom"]
    t4 = temperatures["left"]
    
    integral_fn_x = lambda x : math.sin(n*pi*x)
    integral_fn_y = lambda y : math.sin(n*pi*y)
    
    sum1 = sum2 = sum3 = sum4 = 0

    for n in range(1, 5):
        sum1 += ((math.sinh(n*pi*y)*math.sin(n*pi*x))/math.sinh(n*pi)) * t1 * (integrate.quad(integral_fn_x, 0, 1)[0])
        sum2 += ((math.sinh(n*pi*(1-y))*math.sin(n*pi*x))/math.sinh(n*pi)) * t3 * (integrate.quad(integral_fn_x, 0, 1)[0])
        sum3 += ((math.sinh(n*pi*x)*math.sin(n*pi*y))/math.sinh(n*pi)) * t2 * (integrate.quad(integral_fn_y, 0, 1)[0])
        sum4 += ((math.sinh(n*pi*(1-x))*math.sin(n*pi*y))/math.sinh(n*pi)) * t4 * (integrate.quad(integral_fn_y, 0, 1)[0])

    return 2*(sum1+sum2+sum3+sum4)

def get_temperatures_I(temperatures, size):
    
    step = 1 / (size-1)
    interval = np.arange(step, 1.0, step)[0:(size-2)]

    results_matrix = []
    for y in interval:
        row = []
        for x in interval:
            t = sumation(temperatures, x, y)
            row.append(t)
        results_matrix.insert(0, row)   

    return np.array(results_matrix).flatten()
    

def get_temperatures_II(size, source):
    step = 1 / (size-1)
    interval = np.arange((-1/2), 1/2, step)[1:(size-1)]
    
    pi = math.pi
    a = 1/2
    
    results_matrix = []
    for y in interval:
        row = []
        for x in interval:
            sum=0
            for n in range(0, 5):
                X = x/a
                Y = y/a
                sum += (((-1)**n)*math.cosh((2*n + 1)*pi/2*X)*math.cos((2*n+1)*pi/2*Y))/((((2*n+1)*pi/2)**3)*math.cosh((2*n+1)*pi/2))
            t= (1/2)*(1-Y**2) - 2*sum
            row.append(source*(a**2)*t)
        
        results_matrix.insert(0, row)   
    return np.array(results_matrix).flatten()

def build_final_matrix(results):
    results_index = 0
    size =np.int(np.sqrt(np.array(results).size))
    final_matrix = np.zeros((size, size), dtype=np.int)

    
    if size == 1:
        final_matrix[0,0] = results[0]
    else:
        x = 0
        for column in final_matrix:
            y = 0
            for row in column:
                if y < size:
                    final_matrix[x, y] = results[results_index]
                    results_index += 1
                    
                y += 1
            x += 1


    return final_matrix

    