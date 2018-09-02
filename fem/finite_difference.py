import numpy as np
import functools


def diferencias_finitas(size, temperatures, source):

    matrix = create_matrix_from_inputs(temperatures, size)
    constant_matrix = build_constant_matrix(matrix, source)
    coeficient_matrix = build_coeficient_matrix(constant_matrix, matrix)
    results = get_results(constant_matrix, coeficient_matrix)
    final_matrix = build_final_matrix(results)

    return final_matrix

def create_matrix_from_inputs(temperatures, size):
    matrix = np.zeros((size, size), dtype=np.int)
    x = 0
    for column in matrix:
        y = 0
        for row in column:
            matrix[y, x] = choose_temperature(temperatures, x, y, size)
            y += 1
        x += 1

    return matrix

def build_constant_matrix(matrix, source):
    constants = []
    y = 0
    for row in matrix:
        x = 0
        for column in row:
            if node_in_border(matrix, x, y):
                pass
            else:
                constante = sum_border_nodes(matrix, x, y)
                constants.append(constante)
            x += 1
        y += 1
    element_area = (1 / (np.sqrt(np.array(matrix).size) -1)) ** 2
    
    return np.array(constants) + (source * element_area) 

def build_coeficient_matrix(constant_matrix, matrix):
    matrix_coeficients = []

    y = 0
    for row in matrix:
        x = 0
        for column in row:
            if node_in_border(matrix, x, y):
                pass
            else:
                if node_in_border(matrix, x  , y-1): 
                    neighbour_1 = None
                else:
                    neighbour_1 = {"x": x  , "y" : y-1}

                if node_in_border(matrix, x+1, y  ):
                    neighbour_2 = None
                else:
                    neighbour_2 = {"x": x+1, "y" : y  }
                    
                if node_in_border(matrix, x  , y+1):
                    neighbour_3 = None
                else: 
                    neighbour_3 = {"x": x  , "y" : y+1}
                
                if node_in_border(matrix, x-1, y  ): 
                    neighbour_4 = None
                else: 
                    neighbour_4 = {"x": x-1, "y" : y  }

                neighbours = [neighbour_1, neighbour_2, neighbour_3, neighbour_4]
                     
                coeficient_row = coeficients_row(constant_matrix, matrix, x, y, neighbours)
                matrix_coeficients.append(coeficient_row)
            x += 1
        y += 1
        
    return np.array(matrix_coeficients)
   
def get_results(constant_matrix, coeficient_matrix):
    return np.linalg.solve(np.array(coeficient_matrix), np.array(constant_matrix))

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

def coeficients_row(constant_matrix, matrix, x, y, neighbours):
    coeficients_row = np.zeros(np.int(constant_matrix.size))
    matrix_size = np.int(np.sqrt(constant_matrix.size))
    current_node_index = matrix_index_to_array_index(matrix_size, x, y)
    coeficients_row[np.int(current_node_index)] = 4

    for neighbour in neighbours:
        if neighbour!= None:
            neighbour_index = matrix_index_to_array_index(matrix_size, neighbour["x"], neighbour["y"])
            coeficients_row[np.int(neighbour_index)] = -1

    return coeficients_row

def matrix_index_to_array_index(matrix_size, x, y):
    return (x-1) + (y-1) * matrix_size

def sum_border_nodes(matrix, x, y):
    array = [
        get_node_by_indexes(matrix, x    , y - 1), 
        get_node_by_indexes(matrix, x + 1, y), 
        get_node_by_indexes(matrix, x    , y + 1), 
        get_node_by_indexes(matrix, x - 1, y)
    ]
    return functools.reduce(lambda x, y: x + y, array)

def get_node_by_indexes(matrix, x, y):
    return matrix[y,x]

def node_in_border(matrix, x, y):
    '''True if the node is in any border'''
    size = np.sqrt(matrix.size)
    return (x == 0 or y == 0 or y == size -1 or x == size - 1)

def choose_temperature(temperatures, x, y, size):
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
