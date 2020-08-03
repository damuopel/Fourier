from svgpathtools import svg2paths, wsvg
import numpy as np
import matplotlib.pyplot as plt

paths, attributes = svg2paths('Import.svg')

Path = paths[0]

plt.ion()

for i in np.arange(0,1,0.01):

    point = Path.point(i)

    x = np.real(point)
    y = np.imag(point)
    

    plt.plot(x,y,'bo')
    
    plt.draw()
    plt.pause(1e-6)