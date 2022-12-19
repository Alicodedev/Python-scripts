import matplotlib.pyplot as plt
import numpy as np
amount = 15
lst = np.random.randint(0,100,amount)
x = np.arange(0,amount,1)

n = len(lst)
 
# Traverse through all array elements
for i in range(len(n)):
 
 # Find the minimum element in remaining
 # unsorted arrayy
 
    min_idx = i
    for j in range(i+1, len(n)):
        plt.bar(x,lst)
        plt.pause(0.01)
        plt.clf()

        if n[min_idx] > n[j]:
                min_idx = j

 # Swap the found minimum element with
 # the first element  
plt.show()

