#Script for BinarySearch algorithm in python
"""
     **Using sorted array
     **It returns index of x in given array array_A if present, 
     **else returns -1 
"""
def BinarySearch(array_A,key_C):
    First=0
    Last=len(array_A)-1
   
    
    while First <= Last:
        Middle = (First+Last)//2
        if(array_A[Middle] == key_C): # If element is present at the Middle itself
            return Middle  
        elif(array_A[Middle] > key_C): #if key_C is greater,ignore 1st possibility
            Last = Middle - 1
        else:
            First = Middle + 1  #if key_C is smaller, ignore 2nd possibility
    return -1              # If we reach here, then the element was not present    
    
      
array_A=[1,2,3,4,5,6]   #Test array
print(array_A)
key_C = int(input("Enter the key:"))   

print(BinarySearch(array_A,key_C))  #function call


