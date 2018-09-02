import numpy as np


def galerkin(size, temperatures, source):
    size = size
    matrix = [[ 4,-1,-2,-1],[-1, 4,-1,-2],[-2,-1, 4,-1],[-1,-2,-1,4]]
    element_stifness_matrix = np.array(matrix)*1/6

    stiffness_and_force_matrix = stiffness_and_forces_matrix(size, element_stifness_matrix, source)
    
    temperature_array = create_temperature_array(size, temperatures)

    final_problem_matrixes = final_problem_arrangement(temperature_array, stiffness_and_force_matrix)

    results = get_results(final_problem_matrixes["final_stiffness_matrix"], final_problem_matrixes["final_temperature_indexes"], stiffness_and_force_matrix["forces_array"])
    final_matrix = build_final_matrix(results)
    
    return final_matrix

def stiffness_and_forces_matrix(size, element_stifness_matrix, source):
    '''Metodo que obtiene la matriz de rigidez y el array de fuerzas ensamblados'''
    stiffness_matrix_size = np.square(size)
    stiffness_matrix = np.zeros((stiffness_matrix_size, stiffness_matrix_size))
    elements = get_elements_array(size)
    stiffness_matrix_indexes = get_stiffness_matrix_indexes(size, elements)

    elements = np.square(size-1)
    element_area = (1/elements)

    forces_array = np.zeros(stiffness_matrix_size)

    for y in  range(0, len(stiffness_matrix_indexes)):
        m = sorted(stiffness_matrix_indexes[y])
        
        i = 0
        for x in m:
            forces_array[x] += (source*element_area)/4
            j=0
            for z in m:
                stiffness_matrix[z, x] += element_stifness_matrix[j, i]

                j+=1

            i+=1

    return {"stiffness_matrix": stiffness_matrix, "forces_array": forces_array }       

def create_temperature_array(size, temperatures):
    '''Crea un array de temperaturas si son conocidas o coordenadas si son incognita'''
    temperature_array = []
    for y in range(0, size):
        for x in range(0, size):
            if node_in_border(size, x, y):
              temperature_array.append(choose_temperature(size, temperatures, x, y))
            else:
              temperature_array.append([x, y])              
    return temperature_array
    
def final_problem_arrangement(temperature_array, stiffness_and_forces_matrix):
    stiffness_matrix = stiffness_and_forces_matrix["stiffness_matrix"] 
    final_temperature_indexes = []

    t = 0
    for z in range(0, len(temperature_array)):
        temperature = temperature_array[z]
        if type(temperature) != list:

            for y in range(0, len(stiffness_matrix)):
                for x in range(0, len(stiffness_matrix)):
                    if x == t:
                        stiffness_matrix[y,z] *= temperature
            
        else:
            final_temperature_indexes.append(z)
            
        t += 1

    return {"final_stiffness_matrix": stiffness_matrix, "final_temperature_indexes": final_temperature_indexes } 

def get_results(final_stiffness_matrix, final_temperature_indexes, forces_array):
    matrix = []
    forces = []

    #recorro la matriz por cada indice
    for y in range(0, len(forces_array)):
        #si el indice esta en la lista de indices
        if y in final_temperature_indexes:
            #sumo los valores de las constantes
            acc = 0
            for x in range(0, len(forces_array)):
                if x not in final_temperature_indexes:
                    acc += final_stiffness_matrix[y, x]
                else:
                    matrix.append(final_stiffness_matrix[y, x])
            forces.append(forces_array[y] - acc)
    
    size = np.sqrt(np.array(matrix).size)
    matrix = np.reshape(matrix, (int(size), int(size)))

    if len(forces) == 1:
        result = [forces[0]/matrix[0]]
    else:
        result = np.linalg.solve(np.array(matrix), np.array(forces))                
    return result

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

def get_nodes_by_element(element):
    '''Devuelve las coordenadas de los 4 nodos de un elemento'''
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
    '''Devuelve los indices de la matriz ensamblada en los cuales se suman los componentes de las matrices de cada elemento'''
    stiffness_matrix_indexes = []
    
    for element in elements:
        nodes = get_nodes_by_element(element)
        column = []
        for node in nodes:
            column.append(element_to_stiffness_indexes(size, node))
        stiffness_matrix_indexes.append(column)
    return(stiffness_matrix_indexes)

def node_in_border(size, x, y):
    '''True if the node is in any border'''
    return (x == 0 or y == 0 or y == size -1 or x == size - 1)

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
