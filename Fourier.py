from svgpathtools import svg2paths
import numpy as np
import matplotlib.pyplot as plt
import gif
import sys
from os import path, getcwd

originPath = path.join(getcwd(),'Examples',sys.argv[1])
paths, attributes = svg2paths(originPath)

Path = paths[0]

n = 200
auxN = np.arange(1,np.ceil(n/2.0)+1)
N = np.append(0,np.array([auxN,-auxN]).T.flatten())

cReal = np.zeros(N.size)
cImag = np.zeros(N.size)

incT = 0.001
for index, iN in enumerate(N):
    ic = 0
    for iT in np.arange(0,1,incT):
        ic += Path.point(iT)*np.exp(-iN*2*np.pi*1j*iT)*incT
    cReal[index] = np.real(ic)
    cImag[index] = np.imag(ic)
    
t = np.arange(0,1,incT)
x = np.zeros((t.size,N.size))
y = np.zeros((t.size,N.size))
xf = np.zeros(t.size)
yf = np.zeros(t.size)
for i,iT in enumerate(t):
    value = 0
    for j, iN in enumerate(N):
        value += complex(cReal[j],cImag[j])*np.exp(-iN*2*np.pi*1j*iT)
        x[i,j] = np.real(value)
        y[i,j] = -np.imag(value)
        
xf = x[:,-1]      
yf = y[:,-1]  
              
@gif.frame
def plot(i):
    plt.figure()
    scale = 1
    plt.xlim((np.round(scale*min(xf)),np.round(scale*max(xf))))
    plt.ylim((np.round(scale*min(yf)),np.round(scale*max(yf))))
    plt.axis('off')
    plt.plot(xf[:i],yf[:i],'b')
    for j in range(1,N.size): 
        plt.plot(x[i,j-1:j+1],y[i,j-1:j+1],'r')

frames = []
for i in np.arange(0,t.size,1):
    frame = plot(i)
    frames.append(frame)

finalPath = path.join(getcwd(),'GIFs',sys.argv[2])
gif.save(frames,finalPath,duration=50)