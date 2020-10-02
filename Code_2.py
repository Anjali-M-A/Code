
#Related to Definitions
#Variables in python is object


a=12              #Definition of Variables
print(int(a))
_a_Value=2        #naming conventions
print(_a_Value)

Anju4=3       
print(Anju4)

aGVar = "global "    #global variable    #camel case

def SampleFunction():
    
    global a_GVar
    
    ALVar= "local"    #local variable    #pascal case
    
    a_GVar = aGVar * 2  #Sequential case
    
    print("scope of the variable is ",aGVar),print("scope of the variable is",ALVar)  #multiline
    
    print("scope of the global variable twice",a_GVar)   #singleline
    
SampleFunction()




 
