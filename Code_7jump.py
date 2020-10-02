# Python code to implement Jump Search
"""
   ** Time complexity - O(√n)
   
   ** Input :
        # Sorted array - arr
        # x - search value
        # step - jump size
        # n - length of array
        
    **Importatnt Points:
        # Works only sorted arrays
        # The time complexity of Jump Search is between Linear Search ((O(n)) and Binary Search (O(Log n))
           *(O(Log n)) > O(√n) > ((O(n))
"""        
#math module is used to access mathematical functions in the Python    
import math 
  
def jumpSearch( arr , x , n ):  
      
    # Finding block size to be jumped 
    step = math.sqrt(n)
    
    # Finding the block where element is present (if it is present) 
    first = 0
    
    # while loop to do something as long as the condition is met
    # min() function returns the smallest of the input values
    while arr[int(min(step, n)-1)] < x:   
        first = step 
        step = step + 1 
        
    # Doing a linear search for x in block beginning with first.    
    while arr[int(first)] < x: 
        first = first + 1
          
        # If we reached next block or end of array, 
        # element is not present. 
        if first >= min(step, n): 
            return -1
      
    # If element is found 
    if arr[int(first)] == x: 
        return first 
      
    return -1
  
# input or pre-requirements 
arr = [ 1,2,3,4,5,6,7,8,9 ] 
x = 4
n = len(arr) 
  
# Find the index of 'x' using Jump Search 
index = jumpSearch(arr, x, n) 
  
# Print the index where 'x' is located 
print("Number" , x, "is at index" ,"%.0f"%index)

print("Number" , x, "is at index" , + index)
  
