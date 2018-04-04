import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

import shutil
import os

def create_plot(results):
    plt.clf()
    results_array = np.array(results)
    size = results_array.size
    result_matrix_size = np.int(np.sqrt(size))
    results_matrix = results_array.reshape(result_matrix_size, result_matrix_size)
    #print(results_matrix)

    """ column_labels = list(range(0,24))
    row_labels = ["Lundi",
                  "Mardi",
                  "Mercredi",
                  "Jeudi",
                  "Vendredi",
                  "Samedi",
                  "Dimanche"] 

    

    data = np.array([[35.         ,29.085612   ,26.34244801 ,24.91091625 ,24.15060983 ,23.86734132, 24.14890562 ,25.54837068],
                    [40.914388   ,35.         ,31.37326379 ,29.15060715 ,27.82418173 ,27.16984985 ,27.17991048 ,28.0445771 ],
                    [43.65755199 ,38.62673621 ,35.         ,32.49406682 ,30.82566012 ,29.80796586 ,29.35630934 ,29.45002723],
                    [45.08908375 ,40.84939285 ,37.50593318 ,35.         ,33.17642606 ,31.88004414 ,30.98733379 ,30.39922248],
                    [45.84939017 ,42.17581827 ,39.17433988 ,36.82357394 ,35.         ,33.54845083 ,32.3137592  ,31.1595289 ],
                    [46.13265868 ,42.83015015 ,40.19203414 ,38.11995586 ,36.45154917 ,35.         ,33.55972328 ,31.92513391],
                    [45.85109438 ,42.82008952 ,40.64369066 ,39.01266621 ,37.6862408  ,36.44027672 ,35.         ,32.98128348],
                    [44.45162932 ,41.9554229  ,40.54997277 ,39.60077752 ,38.8404711  ,38.07486609 ,37.01871652 ,35.        ]])
    print(data)
    """
    
    data = np.array(results_matrix)
    fig, axis = plt.subplots()
     
    heatmap = axis.pcolor(data, cmap=plt.cm.jet) 

    axis.set_yticks(np.arange(data.shape[0])+0.5, minor=False)
    axis.set_xticks(np.arange(data.shape[1])+0.5, minor=False)

    axis.invert_yaxis()

    #axis.set_yticklabels(row_labels, minor=False)
    #axis.set_xticklabels(column_labels, minor=False)

    fig.set_size_inches(5.5, 5)
    plt.colorbar(heatmap)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'plots')
    
    print(path)
    name ='temp-matrix-' + str(np.random.random_integers(50)) + '.png'
    plt.savefig( os.path.join(path, name), dpi=100)

    return '/static/plots/' + name
