import numpy as np
import math

import galerkin
import finite_difference
import resolucion_analitica
import error2

def string_arround(number):
    return str(np.around(number, decimals=2))

def comparacion_entre_metodos(size, temperatures, source, file):
    result1 = np.amax(finite_difference.diferencias_finitas(size, temperatures, source))
    result2 = np.amax(galerkin.galerkin(size, temperatures, source))
    result3 = np.amax(resolucion_analitica.resolucion_analitica(size, temperatures, source))

    methods = {"method": 'analitica', "method2": 'diferencias_finitas'}
    error_average_diferencias_finitas = error2.get_error_average(size, temperatures, source, methods)
    
    methods = {"method": 'analitica', "method2": 'galerkin'}
    error_average_galerkin = error2.get_error_average(size, temperatures, source, methods)
    file.write("Nodos: " + string_arround(size) + ": " + string_arround(result1) + " | " +  string_arround(result2) 
    + " | " + string_arround(result3) + " || " + string_arround(error_average_diferencias_finitas) + " | " 
    + string_arround(error_average_galerkin) + "\n")
    


filename = "log3.txt"
file = open(filename, "w")
file.write("TRABAJO PRACTICO FINAL DE CALCULO POR ELEMENTOS FINITOS\n")
file.close()

file = open(filename, "a")


#------------------------------------------------------------------------------------
file.write("COMPARACION ENTRE METODOS\n")
file.write("CASO 1\n")

temperatures = {"top": 0, "right": 0, "bottom": 0, "left": 0}
fuente = 1000

file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

comparacion_entre_metodos(5, temperatures, fuente, file)

""" 
for n in range (5, 65, 5):
    comparacion_entre_metodos(n, temperatures, fuente)
"""

print("Fin caso 1")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")


#------------------------------------------------------------------------------------

file.close()