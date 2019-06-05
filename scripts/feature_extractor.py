# Jose Menendez
# Feature statistics

def zero_crossing_rate(data):
    import numpy as np
    my_array = np.array(data)
    return ((my_array[:-1] * my_array[1:]) < 0).sum()

def read():
    import os
    import sys
    from os import listdir
    arguments = sys.argv
    dir = "."

    if not arguments[1]:
        sys.exit('Error in path')
    else:
        dir = arguments[1]

    for f in listdir(dir):        
        w_ext = f.split(".")
        if len(w_ext) > 1 and w_ext[1] in ['txt', 'csv']:
             # Open & creation of files
            file = open(os.path.join(dir, f), 'r')
            line = file.readline()
            while line:
                line = file.readline()
                print(line)
read()