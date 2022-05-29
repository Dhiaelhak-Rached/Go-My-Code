import numpy as np
 
array1 = [0,1,2]
array2= [2,1,0]
 
nparray = np.array((array1, array2))
print(nparray)
print(np.cov(nparray))