import numpy as np
import math

import galerkin
import finite_difference
import resolucion_analitica
import error2


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

for n in range (5, 65, 5):
    result1 = np.amax(finite_difference.diferencias_finitas(n, temperatures, fuente))
    result2 = np.amax(galerkin.galerkin(n, temperatures, fuente))
    result3 = np.amax(resolucion_analitica.resolucion_analitica(n, temperatures, fuente))
    file.write("Cantidad de Nodos: " + str(n) + ": " + str(result1) + " | " +  str(result2) + " | " + str(result3) + "\n")

print("Fin caso 1")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")

#------------------------------------------------------------------------------------
file.write("COMPARACION ENTRE METODOS\n")
file.write("CASO 2\n")

temperatures = {"top": 0, "right": 0, "bottom": 0, "left": 0}
fuente = 2000

file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
    result1 = np.amax(finite_difference.diferencias_finitas(n, temperatures, fuente))
    result2 = np.amax(galerkin.galerkin(n, temperatures, fuente))
    result3 = np.amax(resolucion_analitica.resolucion_analitica(n, temperatures, fuente))
    file.write("Cantidad de Nodos: " + str(n) + ": " + str(result1) + " | " +  str(result2) + " | " + str(result3) + "\n")

print("Fin caso 2")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")



#------------------------------------------------------------------------------------
file.write("CASO 3\n")

temperatures = {"top": 10, "right": 10, "bottom": 10, "left": 10}
fuente = 1000

file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
    result1 = np.amax(finite_difference.diferencias_finitas(n, temperatures, fuente))
    result2 = np.amax(galerkin.galerkin(n, temperatures, fuente))
    result3 = np.amax(resolucion_analitica.resolucion_analitica(n, temperatures, fuente))
    file.write("Cantidad de Nodos: " + str(n) + ": " + str(result1) + " | " +  str(result2) + " | " + str(result3) + "\n")


print("Fin caso 3")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")

#------------------------------------------------------------------------------------

file.write("CASO 4\n")

temperatures = {"top": 10, "right": 10, "bottom": 10, "left": 10}
fuente = 0

file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
    result1 = np.amax(finite_difference.diferencias_finitas(n, temperatures, fuente))
    result2 = np.amax(galerkin.galerkin(n, temperatures, fuente))
    result3 = np.amax(resolucion_analitica.resolucion_analitica(n, temperatures, fuente))
    file.write("Cantidad de Nodos: " + str(n) + ": " + str(result1) + " | " +  str(result2) + " | " + str(result3) + "\n")


print("Fin caso 4")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")
file.write("\n")

#------------------------------------------------------------------------------------

file.write("ERROR PROMEDIO\n")
file.write("CASO 5\n")


temperatures = {"top": 0, "right": 0, "bottom": 0, "left": 0}
methods = {"method": 'diferencias_finitas', "method2": 'analitica'}
fuente = 1000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


file.write("\n")


temperatures = {"top": 0, "right": 0, "bottom": 0, "left": 0}
methods = {"method": 'galerkin', "method2": 'analitica'}
fuente = 1000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


print("Fin caso 5")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")
file.write("\n")

#------------------------------------------------------------------------------------
file.write("CASO 6\n")


temperatures = {"top": 10, "right": 10, "bottom": 10, "left": 10}
methods = {"method": 'diferencias_finitas', "method2": 'analitica'}
fuente = 0

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


file.write("\n")


temperatures = {"top": 20, "right": 20, "bottom": 20, "left": 20}
methods = {"method": 'galerkin', "method2": 'analitica'}
fuente = 0

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


print("Fin caso 6")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")
file.write("\n")


#------------------------------------------------------------------------------------

file.write("CASO 6\n")


temperatures = {"top": 20, "right": 30, "bottom": 40, "left": 50}
methods = {"method": 'diferencias_finitas', "method2": 'analitica'}
fuente = 0

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


file.write("\n")


temperatures = {"top": 20, "right": 30, "bottom": 40, "left": 50}
methods = {"method": 'galerkin', "method2": 'analitica'}
fuente = 1000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


print("Fin caso 6")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")
file.write("\n")

#------------------------------------------------------------------------------------

file.write("CASO 7\n")


temperatures = {"top": 20, "right": 30, "bottom": 40, "left": 50}
methods = {"method": 'diferencias_finitas', "method2": 'analitica'}
fuente = 1000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


file.write("\n")


temperatures = {"top": 20, "right": 30, "bottom": 40, "left": 50}
methods = {"method": 'galerkin', "method2": 'analitica'}
fuente = 1000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


print("Fin caso 7")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")
file.write("\n")

 
#------------------------------------------------------------------------------------

file.write("CASO 8\n")


temperatures = {"top": 20, "right": 30, "bottom": 40, "left": 50}
methods = {"method": 'diferencias_finitas', "method2": 'analitica'}
fuente = 2000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


file.write("\n")


temperatures = {"top": 20, "right": 30, "bottom": 40, "left": 50}
methods = {"method": 'galerkin', "method2": 'analitica'}
fuente = 1000

file.write("METODOS A COMPARAR: " + str(methods["method"]) + " | " + str(methods["method2"]) + "\n")
file.write("TEMPERATURAS: " + str(temperatures["top"]) 
			+ ", " + str(temperatures["right"]) 
			+ ", " + str(temperatures["left"]) 
			+ " y " + str(temperatures["bottom"])
			+ "\n")
file.write("FUENTE: " + str(fuente) + "\n")

for n in range (5, 65, 5):
	error_average = error2.get_error_average(n, temperatures, fuente, methods)
	file.write("Cantidad de Nodos: " + str(n) + ": Error Promedio: " +  str(error_average) + "\n")


print("Fin caso 8")
file.write("-----------------------------------------------------------------------------\n")
file.write("\n")
file.write("\n")

#------------------------------------------------------------------------------------

file.close()