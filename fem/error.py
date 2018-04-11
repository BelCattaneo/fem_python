import numpy as np

from . import finite_difference
from . import galerkin


def get_error_matrix(size, temperatures, source):
    finite_difference_results = finite_difference.diferencias_finitas(temperatures, source, size)
    galerkin_results = galerkin.galerkin(size, temperatures, source)
    print(finite_difference_results)
    print(galerkin_results)
    diff = np.subtract(finite_difference_results, galerkin_results)
    print(diff)

    error_matrix = np.zeros((size, size), dtype=np.int)

    for y in range(0, size):
        for x in range(0, size):
            error_matrix[x,y] += (np.absolute(diff[x,y]) / galerkin_results[x,y]) * 100

    return error_matrix