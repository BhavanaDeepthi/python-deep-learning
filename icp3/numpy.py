#use of mode() function
# mode() function a sub-set of the statistics module
# We need to import statistics module before doing any work
import statistics
from statistics import mode
import numpy as np #we import numpy as np


randnums = np.random.randint(0,21,15)#create a variable names randnums and set it to np.random.rand
#here 0 is inclusive 21 is exclusive



print(randnums)# Printing out the entire list
print("Most repeated value is:",statistics.mode(randnums))# Printing out mode of given data-set
