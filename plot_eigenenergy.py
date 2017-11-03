# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:42:30 2017

@author: e0008730

Thanks Han Hoe for giving me this script
"""
"""
#example for sub plot
import matplotlib.pyplot as plt
import numpy as np

def xticklabels_example():
    fig = plt.figure() 

    x = np.arange(20)
    y1 = np.cos(x)
    y2 = (x**2)
    y3 = (x**3)
    yn = (y1,y2,y3)
    COLORS = ('b','g','k')

    for i,y in enumerate(yn):
        ax = fig.add_subplot(len(yn),1,i+1)

        ax.plot(x, y, ls='solid', color=COLORS[i]) 

        if i != len(yn) - 1:
            # all but last 
            ax.set_xticklabels( () )
        else:
            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(14) 
                # specify integer or one of preset strings, e.g.
                #tick.label.set_fontsize('x-small') 
                tick.label.set_rotation('vertical')

    fig.suptitle('Matplotlib xticklabels Example')
    plt.show()

if __name__ == '__main__':
    xticklabels_example()

"""

import sys
if sys.version_info[0] == 2:
    python3_path = ['', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\spyder\\utils\\site', 'C:\\ProgramData\\Anaconda3\\python36.zip', 'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Sphinx-1.5.6-py3.6.egg', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\setuptools-27.2.0-py3.6.egg', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\IPython\\extensions', 'C:\\Users\\e0008730\\.ipython']
    for item in python3_path:
        sys.path.append(item)


import matplotlib.pyplot as plt

#plot in TeX style
plt.rcParams['text.usetex'] = True

#put tick inside the graph
plt.tick_params(direction = 'in')
#set tick lable size
plt.tick_params(labelsize=14)

try:
    myfile = open("eigenvalues.dat","r")
except IOError:
    print("Could not open file! Please close Excel!")

eigen_energy = []

num_states = len(myfile.readline().split())
for i in range(num_states):
    eigen_energy.append([])

for line in myfile:
    datas = [float(x) for x in line.split()]
    count = 0
    for energy in datas:
        eigen_energy[count].append(float(energy))
        count = count + 1   

for i in range(num_states):
    if i%2 == 0:
         plt.plot(eigen_energy[i-1])

plt.savefig('test.png', dpi = 300)

"""
#plot range
x_min = 0
x_max = 6
y_min = 0
y_max = 20 
plt.axis([x_min, x_max, y_min, y_max])
#alternative way
#plt.ylim([y_min, y_max])
#plt.xlim([x_min, x_max])

#use mathematical expression for axis
plt.xlabel(r'$x_i$', fontsize=20)
plt.ylabel(r'$y_i$', fontsize=20)

#data to be plotted
x1 = [1,2,3,4]
y1 = [1,4,9,16]

x2 = [1,2,3,4]
y2 = [6,5,4,3]

#'ro' stands for red circular marker
#see https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot  for details 
plt.plot(x1, y1, 'ro', x2, y2, 'c--')
#plt.show()
plt.savefig('test.png')


"""


