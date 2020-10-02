# Script to demonstrate Recursive Function and  Iterative Function

#Recursive Function
"""
  #function will continue to call itself and repeat its behavior until some condition is met to return a result.
"""
print("Recursive Function")
def counter(c):
    if c<=0:
        return c
    else:
# c is parameter and counter(c-1) is recursive function
        return c+counter(c-1)
    
#Function counter will add 5,4,3,2,1 and it'll give output   
Rcr=counter(5)
print(Rcr)

#Iterative Function
"""
     #Repeated execution of a set of statements 
"""
print("\nIterative Function")

def counter(c):
    Sum=0
    for i in c:
        Sum=Sum+i
    return Sum
print(counter([1,2,3,4,5]))        




