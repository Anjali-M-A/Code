#Script to demonstrate the difference between deep copy and shallow copy
"""
   # Deep Copy -
        **any changes made to a copy of object do not reflect in the original object.
        **the change made in the list did not effect in other lists, indicating the list is deep copied.
 
   # Shallow Copy -
        **any changes made to a copy of object do reflect in the original object.
        **the change made in the list did effect in other list, indicating the list is shallow copied.
        """
print("Deep Copy")

# importing "copy" for copy operations 
import copy 
  
# initializing list 1 
li1 = [[1, 2],3,5, 4] 
  
# using deepcopy to deep copy  
li2 = copy.deepcopy(li1) 
  
print("\r")

  # adding and element to new list 
li2[0][1] = "a"

# original elements of list
print("The original elements before deep copying", li1)

# Change is reflected in l2
print("The new list of elements after deep copying ", li2)

# Change is NOT reflected in original list 
# as it is a deep copy 
print ("The original elements after deep copying") 
print(li1)

print("\r")

######## Shallow Copy #####
print("Shallow Copy")

# importing "copy" for copy operations 
import copy 
  
# initializing list 1 
li1 = [1,2,3,5,4] 
  
# using copy to shallow copy  
li2 = copy.copy(li1) 
    
print("\r") 
  
# adding and element to new list 
li2[1] = 7

# original elements of list 
print ("The original elements before shallow copying",li1)

# checking if change is reflected 
print ("The original elements after shallow copying", li2)

print("\r")
print("Shallow copy on nested list\n")

### Shallow Copy behaves differently when it is applied on the nested list

import copy

lis1 = [[1,2],3,4]

lis2 = copy.copy(lis1)

# changing the value "a" on 0th index i.e,[1,2] in that 1st index i.e,2 
lis2[0][1] = "a"

print("Showing lis1", lis1)
print("Showing lis2", lis2)


 



  
  

