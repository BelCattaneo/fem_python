import numpy as np

def resolucion_analitica(size, temperatures, source):
    results = get_results(size, temperatures, source)

    temp_matrix = create_matrix_from_inputs(temperatures, size)

    final_matrix = build_final_matrix(temp_matrix, results)
    
    return final_matrix

def get_results(size, temperatures, source):
    results_temperature_matrix_size = size-2
    results_matrix = []
    
    t1 = temperatures["top"]
    t2 = temperatures["right"]
    t3 = temperatures["bottom"]
    t4 = temperatures["left"]


    for j in range(0, results_temperature_matrix_size):
        row = []
        for i in range(0, results_temperature_matrix_size):
            x = (i+1)/(results_temperature_matrix_size+1)
            y = (j+1)/(results_temperature_matrix_size+1)

            temp = ((((t2-t4)*(t1-t3))*((x+y)+(x*(1-x)+y*(1-y))))+t4*(t1-t3+t2-t4))/(t1-t3+t2-t4)

            row.append(temp)

        results_matrix.insert(0, row)

    results = np.array(results_matrix).flatten()
    return results

def create_matrix_from_inputs(temperatures, size):
    matrix = np.zeros((size, size), dtype=np.int)
    x = 0
    for column in matrix:
        y = 0
        for row in column:
            matrix[y, x] = choose_temperature(size, temperatures, x, y)
            y += 1
        x += 1

    return matrix

def build_final_matrix(matrix, results):
    results_index = 0
    final_matrix = np.copy(matrix)
    size = np.array(results).size

    
    if size == 1:
        final_matrix[1,1] = results[0]
    else:
        x = 0
        for column in final_matrix:
            y = 0
            for row in column:
                print(np.array(column).size)
                if results_index < size:
                    if (final_matrix[x,y] == 0 and x > 0 and y > 0 and x < np.array(column).size-1 and y < np.array(column).size-1):
                        final_matrix[x, y] = results[results_index]
                        results_index += 1
                    
                    y += 1
            x += 1


    return final_matrix

    
def choose_temperature(size, temperatures, x, y):
    if x == 0 and y == 0:
        return (temperatures["top"] + temperatures["left"]) / 2

    if x == size - 1 and y == size - 1:
        return (temperatures["right"] + temperatures["bottom"]) / 2

    if x == size - 1 and y == 0:
        return (temperatures["right"] + temperatures["top"]) / 2

    if x == 0 and y == size - 1:
        return (temperatures["left"] + temperatures["bottom"]) / 2

    if x == 0:
        return temperatures["left"]

    if x == size - 1:
        return temperatures["right"]

    if y == 0:
        return temperatures["top"]

    if y == size - 1:
        return temperatures["bottom"]

    return 0