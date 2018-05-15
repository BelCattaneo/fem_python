import galerkin
import finite_difference
import resolucion_analitica


size = 10
temperatures = {"top": 20, "right": 20, "bottom": 100, "left": 100}
source = 1000
galerkito = galerkin.galerkin(size, temperatures, source)
print(galerkito)
diferencito = finite_difference.diferencias_finitas(temperatures, source, size)
print(diferencito)
results = resolucion_analitica.resolucion_analitica(size, temperatures, source)
print(results)