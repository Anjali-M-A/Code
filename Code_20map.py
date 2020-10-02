# Script to demonstrate the map()function
"""
   **The map() function applies a given function to each item of an iterable (list, tuple etc)
    and returns a list of the results.

   **Syntax:
       map(function, iterable, ...)

       #function - map() passes each item of the iterable to this function.
       #iterable - iterable which is to be mapped

"""

#---- Using map() without lambda function----

list_A =[1,2,3,4]

# Squaring of elements in 'list'
def square(x):

#bcz we want to find out the square of the numbers in list
     return x*x
     
print(map(square,list_A))  #it'll return iterator

#In python 3,if we want to get the output as list
print(list(map(square,list_A)))


#----- Using map() with lambda function -----
print("\nUsing map() with lambda function")
"""
    ** taking lambda with 1 argument 'x'and expression'x*x'-this is our function
    ** list_A - our list
"""
print(list(map(lambda x:x*x,list_A)))

# We can use more than 1 tuple or list in map() function
print("\r")
"""
   ** here we are adding another list- list_B
       # when we are adding 2 list
         ** Both the list should have same length via same number of elements in both the list
         ** We can't add string and integer value,both list should contain numbers like int or float
         ** Or both list should contain strings
"""        
list_B =[1,1,1,1]
# taking lambda with 2 arguements 'x' and 'y' with expression 'x+y' and our 2 list-list_A & list_B
print(list(map(lambda x,y:x+y,list_A,list_B)))

#To conver our output to tuple 
print(tuple(map(lambda x,y:x+y,list_A,list_B)))



