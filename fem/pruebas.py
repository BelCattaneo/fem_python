import numpy as np
import math

import galerkin
import finite_difference
import resolucion_analitica
import error2

def string_arround(number):
    return str(format(number, '.2f')).ljust(5)

def comparacion_entre_metodos(size, temperatures, source, file):
    result1 = np.amax(finite_difference.diferencias_finitas(size, temperatures, source))
    result2 = np.amax(galerkin.galerkin(size, temperatures, source))
    result3 = np.amax(resolucion_analitica.resolucion_analitica(size, temperatures, source))

    methods = {"method": 'analitica', "method2": 'diferencias_finitas'}
    error_average_diferencias_finitas = error2.get_error_average(size, temperatures, source, methods)
    
    methods = {"method": 'analitica', "method2": 'galerkin'}
    error_average_galerkin = error2.get_error_average(size, temperatures, source, methods)
    file.write("Nodos: " + string_arround(size).rjust(2) + ": " + string_arround(result1) + " | " +  string_arround(result2) 
    + " | " + string_arround(result3) + " || " + string_arround(error_average_diferencias_finitas) + " | " 
    + string_arround(error_average_galerkin) + "\n")
    

casos = [
    {
        "id": 1,
        "fuente": 1000,
        "temperatures" : {"top": 0, "right": 0, "bottom": 0, "left": 0}
    }, 
     {
        "id": 2,
        "fuente": 5000,
        "temperatures" : {"top": 0, "right": 0, "bottom": 0, "left": 0}
    }, 
     {
        "id": 3,
        "fuente": 0,
        "temperatures" : {"top": 10, "right": 10, "bottom": 10, "left": 10}
    }, 
     {
        "id": 4,
        "fuente": 0,
        "temperatures" : {"top": 50, "right": 50, "bottom": 50, "left": 50}
    }, 
     {
        "id": 5,
        "fuente": 1000,
        "temperatures" : {"top": 10, "right": 10, "bottom": 10, "left": 10}
    }, 
     {
        "id": 6,
        "fuente": 5000,
        "temperatures" : {"top": 50, "right": 50, "bottom": 50, "left": 50}
    }
]
filename = "log3.txt"
file = open(filename, "w")
file.write("TRABAJO PRACTICO FINAL DE CALCULO POR ELEMENTOS FINITOS\n")
file.close()

file = open(filename, "a")

#------------------------------------------------------------------------------------
file.write("COMPARACION ENTRE METODOS\n")
file.write("\n")
for caso in casos:
    file.write("CASO " + str(caso["id"]) + "\n")
    temperatures = caso["temperatures"]
    
    file.write("TEMPERATURAS: " + str(temperatures["top"]) 
                + ", " + str(temperatures["right"]) 
                + ", " + str(temperatures["bottom"]) 
                + " y " + str(temperatures["left"])
		    	+ "\n")
    file.write("FUENTE: " + str(caso["fuente"]) + "\n")
    file.write("\n")

    for n in range (5, 15, 5):
        comparacion_entre_metodos(n, temperatures, caso["fuente"], file)
    
    print("Fin caso " + str(caso["id"]) + "\n") 
    file.write("-----------------------------------------------------------------------------\n")
    file.write("\n")
#------------------------------------------------------------------------------------

file.close()