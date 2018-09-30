import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

import shutil
import os

def create_plot(final_matrix):
    plt.clf()
    """ Si mando array de resultados uso esta parte. """
    """results_array = np.array(results)
    size = results_array.size
    result_matrix_size = np.int(np.sqrt(size))
    results_matrix = results_array.reshape(result_matrix_size, result_matrix_size) """
    

    data = np.array(final_matrix)
    print(data)
    fig, axis = plt.subplots()
     
    heatmap = axis.pcolor(data, cmap=plt.cm.jet) 
    print(heatmap)
    axis.invert_yaxis()

    plt.axis('off')
    
    
    plt.colorbar(heatmap)
    fig.set_size_inches(6.5, 5)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'plots')
    print(path)
    name ='temp-matrix-' + str(np.random.random_integers(50)) + '.png'
    plt.savefig( os.path.join(path, name), dpi=100)

    return '/static/plots/' + name


