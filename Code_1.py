"""
This is the program which is used for comliation process

"""

#function -for addition operation(sample)
#using the keyword def followed by fuction name followed by parathensis

#when we writing a function
#we can follow _ alphabets
#camel case

""" your function name is my function

   in python my_Function(

   Fshould be cample bcz of camel case"""

#defines a function


import dis
def sample():

   a=1 #dynamically typed
   b=3

   sum1 = a+b

   print(sum1)
   
#to call the function
print(sample.__code__.co_code)

print(dis.opname[sample.__code__.co_code[1]])


   
