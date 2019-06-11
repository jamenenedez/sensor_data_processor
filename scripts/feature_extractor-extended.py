# Jose Menendez
# Feature statistics

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def zero_crossing_rate(data):
    import numpy as np
    my_array = np.array(data)
    return ((my_array[:-1] * my_array[1:]) < 0).sum()


def standar_deviation(data):
    import statistics
    return statistics.stdev(data)


def qmean(data):
    import math
    return math.sqrt(sum(n*n for n in data)/len(data))


def arithmetic_mean(data):
    import statistics
    return statistics.mean(data)


def magnitude(x, y, z):
    import math
    return round(math.sqrt(pow(float(x), 2) + pow(float(y), 2) + pow(float(z), 2)), 3)


def read():
    import os
    import sys

    arguments = sys.argv
    dir = "."

    if not arguments[1]:
        sys.exit('Error in path')
    else:
        dir = arguments[1]

    directories = []

    resultDir = os.getcwd()+"/../results"
    if not os.path.isdir(resultDir):
        os.mkdir(resultDir)

    descriptor = open(resultDir+'/descriptor.csv', 'w')
    descriptor.write("arithmetic_average,standard_deviation,mean_squares,class\n")
    
    movilFile = open(resultDir+'/movil.csv', 'w')
    movilFile.write("Bajando escaleras,Bajando pendiente,Caminando,Subiendo escaleras,Subiendo pendiente\n")
    
    smartwatchFile = open(resultDir+'/smartwatch.csv', 'w')
    smartwatchFile.write("Bajando escaleras,Bajando pendiente,Caminando,Subiendo escaleras,Subiendo pendiente\n")
    
    sensorFile = open(resultDir+'/sensor.csv', 'w')
    sensorFile.write("Bajando escaleras,Bajando pendiente,Caminando,Subiendo escaleras,Subiendo pendiente\n")

    for r, d, f in os.walk(dir):
        directories.append(r)

    for d in directories:
        tokens = d.split("\\")
        if len(tokens) == 4:
            sensor = tokens[2]
            action = tokens[3]
            if sensor == "movil":
                movil_dir = os.path.join(dir, str(sensor), str(action))
                
                downstair = []
                downhill = []
                walking = []
                upstair = []
                uphill = []
                
                for m_f in os.listdir(movil_dir):
                    data = []
                    file = open(os.path.join(movil_dir, m_f), 'r')
                    line = file.readline()

                    while line != "":
                        line = file.readline()
                        values = line.split(",")
                        if 4 in range(-len(values), len(values)) and is_number(values[4]):
                            data.append(float(values[4]))
                            if str(action) == "bajando_escaleras":
                               downstair.append(float(values[4]))
                            elif str(action) == "bajando_escaleras":
                                downhill.append(float(values[4]))
                            elif str(action) == "bajando_escaleras":
                                walking.append(float(values[4]))
                            elif str(action) == "bajando_escaleras":
                                upstair.append(float(values[4]))
                            elif str(action) == "bajando_escaleras":                                
                                uphill.append(float(values[4]))
                    
                    row = [str(arithmetic_mean(data)), str(standar_deviation(data)), str(qmean(data)), str(action)]        
                    descriptor.write(",".join(row)+"\n")
            elif sensor == "reloj":
                smart_watch_dir = os.path.join(dir, str(sensor), str(action))
                for sw_f in os.listdir(smart_watch_dir):
                    data = []
                    file = open(os.path.join(smart_watch_dir, sw_f), 'r')
                    line = file.readline()

                    while line != "":
                        line = file.readline()
                        values = line.split(",")
                        if 3 in range(-len(values), len(values)) and is_number(values[3]):
                            data.append(float(values[3]))
                    
                    row = [str(arithmetic_mean(data)), str(standar_deviation(data)), str(qmean(data)), str(action)]        
                    descriptor.write(",".join(row)+"\n")
            elif sensor == "sensor_1":
                inertial_sensor_dir = os.path.join(dir, str(sensor), str(action))
                for is_f in os.listdir(inertial_sensor_dir):
                    data = []
                    file = open(os.path.join(inertial_sensor_dir, is_f), 'r')
                    line = file.readline()

                    while line != "":
                        line = file.readline()
                        values = line.split(",")
                        if 5 in range(-len(values), len(values)) and is_number(values[3]) and is_number(values[4]) and is_number(values[5]):
                            data.append(float(magnitude(values[3], values[4], values[5])))
                    
                    row = [str(arithmetic_mean(data)), str(standar_deviation(data)), str(qmean(data)), str(action)]        
                    descriptor.write(",".join(row)+"\n")

read()
