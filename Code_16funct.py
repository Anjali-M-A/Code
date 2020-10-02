# Script to demonstrate Function types with arguments and without arguments

print("Functions with arguments")

# Default Argument
"""
  ** We can provide a default value to an argument by using the assignment operator (=).
"""
def Func(a=3, b=2):
    
    print(a+b)
    
Func()    #calling without arguments

# b value will be changed from 2 to 3
Func(b=3)  #calling with arguments
Func(1,2)


# Keyword Argument
print("\nKeyword Arguments")
"""
  **  we can change the order of passing the arguments without any consequences.
"""

def add(a,b):
    return a+b
print(add(1,2))

def add(b=1,a=2):
    print(a+b)
add()

# Arbitrary Arguments
print("\nArbitrary Arguments")
"""
  *args (Non-Keyword Arguments) - which allow us to pass the variable number of non keyword arguments to function.

  **kwargs (Keyword Arguments) - allows us to pass the variable length of keyword arguments to the function.
"""
print("\n*args")

# *args
def display(*names):
    for name in names:
        print(name)
display('Sabarish Sir','Navya Apthi','Anjali')

print("\r")
print("**kwargs")

# **kwargs
def display(**names):
    
  #items() -returns a view object that contains the key-value pairs of the dictionary,as tuples in a list
    for key,value in names.items():
        print(key,value)
        
display(key1 ='Sharing',key2 ='is',key3 ='caring')

#Using *args and **kwargs in same line to call a function
print("\nBoth *args and **kwargs")

def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs to pass arguments to this function
myFun('Hi','Hello','People',first="Hi",mid="Hello",last="People")

# Positional Arguments
print("\nPositional Arguments")
"""
  * Positional arguments are arguments that need to be included in the proper position or order.
"""
#position of a is 0 and b is 1
def Func(a,b):
    print(a + b)
Func(2,3)

# Functions without arguments
print("\nFunctions without arguments")

#None Value & User Defined Value
def Func(a,b):
    result = a+b
    print(result) 
var = Func(2,3)
print(var)






    
      



      
     
