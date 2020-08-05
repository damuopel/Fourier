from svgpathtools import svg2paths, wsvg
import numpy as np
import matplotlib.pyplot as plt

paths, attributes = svg2paths('Batman.svg')

Path = paths[0]

n = 100
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
           
plt.ion()   

x -= x[0,0]
y -= y[0,0]
xf -= xf[0]
yf -= yf[0]

for i in np.arange(0,t.size,5):
    plt.clf()
    scale = 1
    plt.xlim((np.round(scale*min(xf)),np.round(scale*max(xf))))
    plt.ylim((np.round(scale*min(yf)),np.round(scale*max(yf))))
    plt.axis('off')
    plt.plot(xf[:i],yf[:i],'b')
    for j in range(1,N.size): 
        plt.plot(x[i,j-1:j+1],y[i,j-1:j+1],'r')
    plt.draw()
    plt.pause(1e-6)
plt.show(block = True)    

        
        
        
        
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    