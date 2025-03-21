import numpy as np
import matplotlib.pyplot as plt
import glob

input_path, output_path, extension = 'data/', 'output/', 'png'

files = glob.glob(input_path+'inflammation-*.csv')
files.sort()

# run simple checks
def detect_problems(patient_data):
    """Perform basic tests on one file for patient data"""
    if np.amax(patient_data, axis=0)[0] == 0 and np.amax(patient_data, axis=0)[20] == 20:
        print('suspicious maxima')
    elif np.sum(np.amin(patient_data, axis=0)) == 0:
        print('suspicious minima')
    else: 
        print('passed')
        
# plot mean, max, and min
def plot_graphs(file_name, patient_data):
    """Plot line graph of patient inflamation data for one file"""
    # set up figure
    fig = plt.figure(figsize=(10.0, 3.0))

    # set up plots
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    # plot the mean
    axes1.set_ylabel('average')
    axes1.plot(np.mean(patient_data, axis=0))

    # plot the max
    axes2.set_ylabel('max')
    axes2.plot(np.amax(patient_data, axis=0))

    # plot the min
    axes3.set_ylabel('min')
    axes3.plot(np.amin(patient_data, axis=0))

    fig.tight_layout()

    plt.savefig(output_path + file_name[5:-3] + extension)
    plt.show()

# loop through files, check for error and plot graphs
for file in files:
    
    # get the data
    print(file)
    data = np.loadtxt(fname=file, delimiter=',')
    
    # detect problems and create graph
    detect_problems(data)
    plot_graphs(file,data)
