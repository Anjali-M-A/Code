#Script to demonstrate Python Datatypes
"""
Different datatypes in python:

  *Numeric - int, float, complex
  *Sequence - list, tuple, range
  *Boolean - True and False
  *Binary - bytes, bytearray, memoryview(buffer protocol)
  *Mapping -dictionary
  *Set - set, frozen-set
  *String - literal, characters, strings

"""
"""
    **Methods used here
        *** type -to know the object type of the variable (data type)
        *** isinstance - to check whether two variables are of same datatype or not
"""        
   
"""Numeric Datatype"""

#integer - syntax int()

sample_Integer = 2    
print("Type of num is:", type(sample_Integer))

sample_Integer_Long = 265376387498478937498274938
print(sample_Integer_Long)

print(isinstance(sample_Integer,int))

#float
"""
float - syntax float()
"""

sample_Float = 3.0   
print("Type of num_1 is:", type(sample_Float))

sample_Float_Truncated = 12.213243243464874668376764873487
print(type(sample_Float_Truncated))
print(sample_Float_Truncated)

#complex
"""
  complex - syntax complex()
"""  

num_2 = 3+5j  
print("Type of num_2 is:", type(num_2))
print("The number ", num_2, " is complex number?", isinstance(3+5j, complex))

"""Sequential DataType"""

#list
"""
   ***syntax - [] (explicit)
            or we can use list()
   ***list is mutable and ordered collection of values
   ***operations related to list:
        #search
        #update
        #remove
        #delete
        #slice
"""
"""
   Additional information:
      list([]) or list(())
"""      

list_1 = [1,2,3,4]
list_2 = [1, 1.1, 1+2j, 'Learn']
list_3 = list([1,2,3])
print(list_1)
print(list_2)
print(list_3)

#mutable

list_1[2]=5 #mutable bcz in list we can change the value

ordered_Sample_List = "abcdefghijklmnopqrstuvwxyz"
ordered_List = list(ordered_Sample_List)
print(list_1)

#tuple
"""
    Syntax - tuple()
    We can create tuple -
      *Creating a Tuple with the use of Strings
      *Creating a Tuple with the use of list
      *Creating a Tuple with the use of built-in function
      *Creating a Tuple with nested tuples
"""
"""
      *Tuple is immutable
      *once we define the value we cant change it
"""      

# Creating an empty tuple  
Tuple1 = ()  
print("Initial empty Tuple: ")  
print (Tuple1)  
    
# Creating a Tuple with the use of Strings  
Tuple1 = ('Anjali', 'Annappa')  
print("\nTuple with the use of String: ")  
print(Tuple1)  
    
# Creating a Tuple with the use of list  
list1 = [1, 2, 4, 5, 6]  
print("\nTuple using List: ")  
print(tuple(list1))  
  
# Creating a Tuple with the use of built-in function  
Tuple1 = tuple('Apple')  
print("\nTuple with the use of function: ")  
print(Tuple1)  
  
# Creating a Tuple with nested tuples  
Tuple1 = (0, 1, 2, 3)  
Tuple2 = ('python', 'Sir')  
Tuple3 = (Tuple1, Tuple2)  
print("\nTuple with nested tuples: ")  
print(Tuple3)

#range
"""
   Syntax-range()
"""   

for i in range(5, 10):  
    print(i, end =" ")

print("\r")

"""Boolean Datatype"""

#Data type with one of the two built-in values True or False. 

print(type(True)) 
print(type(False)) 
  

"""Strings"""
"""
     # Creating a String with single Quotes
     # Creating a String with double Quotes
     # Creating a String with triple Quotes
     # Creating String with triple quotes allows multiple lines 
"""     

# Creating a String with single Quotes

String1 = 'Hello World'
print("String with the use of Single Quotes: ")  
print(String1)  
    
# Creating a String with double Quotes

String1 = "I'm a very happy"
print("\nString with the use of Double Quotes: ")  
print(String1)  
print(type(String1)) 
    
# Creating a String with triple Quotes  
String1 = '''I'm Anjali and I'm from shimogha'''
print("\nString with the use of Triple Quotes: ")  
print(String1)  
print(type(String1)) 
  
# Creating String with triple quotes allows multiple lines  
String1 = '''  Python  
             For  
             Life'''
print("\nCreating a multiline String: ")  
print(String1)  

"""Binary DataTypes"""

#bytes

x =(b'abc')
print(x[2])  

#bytearray
b=bytearray(b'''Anj''') 
print(b)
print(memoryview(x))

"""Mapping DataTypes"""

#dictionary
"""
   Syntax - dict()
   *Creating a Dictionary
      **with Integer Keys  
      **with Mixed keys
      **with dict() method
      **with key-values
"""   
   
# Creating a Dictionary with Integer Keys  
Dict = {1: 'Hai', 2: 'Hello', 3: 'People'}  
print("\nDictionary with the use of Integer Keys: ")  
print(Dict)  
    
# Creating a Dictionary with Mixed keys  
Dict = {'Name': 'Anjali', 1: [1, 2, 3, 4]}  
print("\nDictionary with the use of Mixed Keys: ")  
print(Dict)  
    
# Creating a Dictionary with dict() method  
Dict = dict({1: 'Hai', 2: 'Hello', 3:'People'})  
print("\nDictionary with the use of dict(): ")  
print(Dict)  
    
#Creating a dictionary with key-values
dict = {1:'Anjali', 2:'Annappa'};   
print (dict.keys());
print (dict.values());

"""Set DataType"""
"""
   # Syntax -set()
   #Two type:*set is mutable
             *frozen-set is immutable
   # we can create set with
       *the use of a string
       *the use of a List
       *a mixed type of values(Having numbers and strings) 
"""   

sample_set = {"red", "green", "black"}  #mutable 
print(sample_set)

frozen_set = ({"sagar", "shimogha", "karnataka"})  #immutable
print(frozen_set)

# Creating a Set with the use of a String  
set1 = set("HakunaMatata")  
print("\nSet with the use of String: ")  
print(set1)  
  
# Creating a Set with the use of a List  
set1 = set(["Hai", "Hello", "People"])  
print("\nSet with the use of List: ")  
print(set1)  
  
# Creating a Set with a mixed type of values  
  
set1 = set([1, 2, 'Hai', 4, 'Hello', 6, 'People'])  
print("\nSet with the use of Mixed Values")  
print(set1)  


