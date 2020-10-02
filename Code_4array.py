#Script to demonstrate the methods in array
"""
  #Arrays are constrained to a single datatype value
  
  # In Python, we have to import array module because python doesn't support built-in array types
  
  #some important methods in python:
    *append() - to insert new value at end
    *insert() - to insert value at specific position
    *count() - Counts the number of times a particular element appears in array
    *index() - to print index of occurrenece of a element
    *pop() - to remove a element at a specific position
    *remove() - to remove 1st occurrence of a element
    *reverse() - to reverse the array

  #Additional information:
      help(array) - display the built-in module array in python
"""    

import array     #importing "array" from array operation

arr=array.array('i',[1,2,3])   #initializing array with array values
print("The new created array is:",arr)

#append()

arr.append(4)   
print("The appended array is : ", end="")  #end="" means after the print statement it will print a new line
for i in range (0,len(arr)):  #loop through the individual array element
    print (arr[i], end=" ")

print("\r")  #the new line character     
   
#insert()

arr.insert(2,5) 
print ("The array after insertion is : ",end="")
for i in range (len(arr)): 
    print (arr[i], end=" ")

print("\r")  # new line character    
   
#count()

arr.count(2)
print("The number of times 2 appears in array is",arr.count(2))

#index()

arr.index(2)        
print("The index of occurrence of 2 is:",arr.index(2))

#pop()

arr.pop(2)
print ("The array after popping is:",arr); 

#remove()

arr.remove(1) 
print("The array after removing is:",arr)

#remove()

arr.reverse() #using reverse() to reverse the array
print("The array after reversing is:",arr)

