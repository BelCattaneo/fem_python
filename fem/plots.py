import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

import shutil
import os

def create_plot(final_matrix):
    plt.clf()
    print("Lalalaaaaa")
    """ Si mando array de resultados uso esta parte. """
    """results_array = np.array(results)
    size = results_array.size
    result_matrix_size = np.int(np.sqrt(size))
    results_matrix = results_array.reshape(result_matrix_size, result_matrix_size) """
    

    data = np.array(final_matrix)
    fig, axis = plt.subplots()
     
    heatmap = axis.pcolor(data, cmap=plt.cm.jet) 

    axis.invert_yaxis()

    plt.axis('off')
    
    
    plt.colorbar(heatmap)
    fig.set_size_inches(6.5, 5)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'plots')
    name ='temp-matrix-' + str(np.random.random_integers(50)) + '.png'
    plt.savefig( os.path.join(path, name), dpi=100)

    return '/static/plots/' + name
