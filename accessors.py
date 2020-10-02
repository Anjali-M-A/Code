#accessors

import array

sample_Array = array.array('i',[1,2,3,4])

for i in range (len(sample_Array)):
    print(sample_Array[i])

#Decators
    
sample_Array2 = [1,1,1,1]
sample_Array2[0] = 2
print(sample_Array2)
