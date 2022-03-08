import matplotlib.pyplot as plt
import numpy as np
import scipy.io

flattop_start, flattop_end = 50,100

def get_variable(dataset,index):
    a = dataset['post']['zerod'][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_variable_pnbi(dataset):
    a = dataset['post']['zerod'][0][0]['pnbi'][0][0]
    a1 = a.real #nbi injector 1
    a2 = a.imag #nbi injector 2
    a = [float(x[0]) for x in a1+a2]
    return a

def get_average(dataset, index):
    a = get_variable(dataset,index)
    return (np.mean(a[flattop_start:flattop_end]), np.std(a[flattop_start:flattop_end]))

def get_average_pnbi(dataset):
    a = get_variable_pnbi(dataset)
    return (np.mean(a[flattop_start:flattop_end]), np.std(a[flattop_start:flattop_end]))

def plot2axis(y1,y1label,x,xlabel,
              y2,y2label,legend1="lower center",legend2="center right"):
    ax1 = plt.subplot()
    plt.errorbar(x[:,0],y1[:,0],y1[:,1],x[:,1],fmt='o',label=y1label)
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    ax2 = ax1.twinx()
    ax2.errorbar(x[:,0],y2[:,0],y2[:,1],x[:,1],fmt='o',label=y2label,color="green")
    plt.ylabel(y2label)
    ax1.legend(loc=legend1)
    ax2.legend(loc=legend2)
    plt.show()

def getAvg(rangee,keys,folder):
    avgData = np.zeros((len(keys),len(rangee),2))
    for i in rangee:
        data = scipy.io.loadmat("data/"+str(folder)+"/"+str(i)+".mat")
        for j in range(len(keys)):
            if keys[j] == 'pnbi':
                avgData[j,i] = get_average_pnbi(data)
            else:
                avgData[j,i] = get_average(data,keys[j])
    return avgData
