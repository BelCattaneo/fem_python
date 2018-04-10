import numpy as np
import functools

def create_problem_formulation(size):
    stiffness_matrix_size = np.square(size)
    stiffness_matrix = np.zeros((stiffness_matrix_size, stiffness_matrix_size))

    temperature_array = np.zeros(size*size)

    forces_array = np.zeros(size*size)

    matrix = [4,-1,-2,-1],[-1,4,-1,-2],[-2,-1,4,-1],[-1,-2,-1,4]
    element_stifness_matrix = np.array(matrix)/6
    

    stiffness_matrix = assembly_matrix(size, element_stifness_matrix)

def assembly_matrix(size, element_stifness_matrix):
    stiffness_matrix_size = np.square(size)
    stiffness_matrix = np.zeros((stiffness_matrix_size, stiffness_matrix_size))
    elements = get_elements_array(size)
    stiffness_matrix_indexes = get_stiffness_matrix_indexes(size, elements)
    for y in  range(0, len(stiffness_matrix_indexes)):
        m=stiffness_matrix_indexes[y]
        print(m)
        
        i = 0
        for x in m:
            n = stiffness_matrix_indexes[0]
            stiffness_matrix[m, x] += element_stifness_matrix[i, y] 
            i+=1
    return stiffness_matrix        


def get_nodes_by_element(element):
    return [
        [element[0]    , element[1]    ], 
        [element[0] + 1, element[1]    ],
        [element[0]    , element[1] + 1],
        [element[0] + 1, element[1] + 1]
    ]

def get_elements_array(size):
    elements = []
    for x in range(0, size - 1):
        for y in range(0, size - 1):
            elements.append([x, y])
    return elements

def element_to_stiffness_indexes(size, indexes):
    return indexes[0] * size + indexes[1] 

def get_stiffness_matrix_indexes(size, elements):
    stiffness_matrix_indexes = []
    
    for element in elements:
        nodes = get_nodes_by_element(element)
        column = []
        for node in nodes:
            column.append(element_to_stiffness_indexes(size, node))
        stiffness_matrix_indexes.append(column)
    return(stiffness_matrix_indexes)


[   [ 0.66666667, -0.33333333,  0.        , -0.16666667, -0.16666667,         0.        ,  0.        ,  0.        ,  0.        ],
    [ 0.66666667, -0.5       , -0.16666667, -0.16666667,  0.5       ,        -0.33333333,  0.        ,  0.        ,  0.        ],
    [ 0.        , -0.16666667, -0.16666667,  0.        ,  0.66666667,        -0.33333333,  0.        ,  0.        ,  0.        ],
    [ 0.66666667, -0.33333333,  0.        , -0.5       ,  0.5       ,         0.        , -0.16666667, -0.16666667,  0.        ],
    [ 0.66666667, -0.5       , -0.16666667, -0.5       ,  1.        ,        -0.5       , -0.16666667, -0.5       ,  0.66666667],
    [ 0.        , -0.16666667, -0.16666667,  0.        ,  0.5       ,        -0.5       ,  0.        , -0.33333333,  0.66666667],
    [ 0.        ,  0.        ,  0.        , -0.33333333,  0.66666667,         0.        , -0.16666667, -0.16666667,  0.        ],
    [ 0.        ,  0.        ,  0.        , -0.33333333,  0.5       ,        -0.16666667, -0.16666667, -0.5       ,  0.66666667],
    [ 0.        ,  0.        ,  0.        ,  0.        , -0.16666667,        -0.16666667,  0.        , -0.33333333,  0.66666667]])