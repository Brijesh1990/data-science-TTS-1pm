import matplotlib.pyplot as plt 
import numpy as np 
# draw a line in diagram from position (0,0) to position(6,250)  
# xpoints=np.array([0,10]) 
# ypoints=np.array([0,500])

# xpoints=np.array([0,10]) 
# ypoints=np.array([100,500])

# draw plot without line 

xpoints=np.array([0,10]) 
ypoints=np.array([100,500])

# display in plot
# pass an arguments string it meanse 'rings'
plt.plot(xpoints,ypoints,'o')
plt.show()