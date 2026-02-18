import numpy as np 
import random
# ex1 = np.random.randint(0,100,size=(5,4))

# print(ex1)

arr1 = np.array([[67 ,26 ,27 ,69],
[78, 47, 81 ,68],
[55 ,98, 44 ,33],
[52 ,55 ,96 ,51],
[65 ,81,74 , 92]])

mean = np.mean(arr1)
print(mean)
mean2 = np.mean(arr1 ,axis=0) # 0 for colum
print(mean2)
mean3 = np.mean(arr1,axis=1) #1 for row 
print(mean3)
# Standard deviation [how far is your value from mean]
std = np.std(arr1)
print(std)
std2 = np.std(arr1,axis=0)
print(std2)

# variance

var = np.var(arr1)
print(var)

mima = np.min(arr1) , np.max(arr1)
print(mima)

