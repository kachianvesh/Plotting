import numpy as np 
from matplotlib import pyplot as plt 
x = np.arange(1,11) 
y = 2 * x + 5
#print("Elements are :", x)
#print("Slope values are:", y)
plt.title("Matplotlib demo") 
plt.xlabel("Values of slope") 
plt.ylabel("Slope") 
plt.bar(x,y,color='c') 
plt.show()
