# Script to demonstrate control flow statements
"""
   **The control flow of a Python program is regulated by
        #conditional statements - if, elif, else, nested if
           ** Nature of condition - Boolean(True or False)
           
        #loops - while, for
        
        #function calls(miscellaneous)- pass, break, continue
        
   ** Advantage:
        # In python 3, with while and for loops we can use 'else:' statement
"""

# if Condition(if only)
print("if condition")

marks = 90
if marks == 100:
    print("Perfect")
print("Thank You") # To end the if block


# else Condition
"""
   **the else condition can be optionally used to define an alternate block of statements to be executed
      if the boolean expression in the if condition is not true.
"""
print("\nelse condition")

marks =54
if marks>=35:
    print("Congo..pass")
else:
    print("sorry..fail")

# elif statement(multipossibility)
"""
  **used to include multiple conditional expressions between if and else.
"""
print("\nelif condition")

x = 20
y = 45
z = 23
if x>y and x>z:   #and - logical Operator
    print("x is greater")
    
# if the 'if'statement is not true then it'll check for another condition in elif
elif z>y:
    print("z is greater")
else:
    print("y is greater")

#nested if statements
print("\nnestedif condition")    
"""
   **A nested if is an if statement that is the target of another if statement

   ** Nested if statement means an if statement inside another if statement
"""
#printing marks of a student of a particular college
name = "medhu"
clg = "xyz"
marks = 88
if clg == "xyz":
    if name == "medhu":  # if both 'if' condition is true then it'll print marks of that student
        
        print("medhu of xyz college got:", marks,"marks")
# if any one of condition fails then it'll print bellow statement
    else:
        print("Incorrect Information")

#-----loops----

# while loop
print("\nwhile loop")
"""
  **A while-loop executes a block of code so long as a condition remains True.

  **Syntax :
    while expression:
        statement(s)
"""
count = 1
while count < 3:
    print(count)
    count+= 1     #incrementing the count value
    
else:
    print("goodbye")

#for loop
"""
  **A for loop is used for iterating over a sequence
     (that is either a list, a tuple, a dictionary, a set, or a string).

  ** With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.    
  **Syntax:

      for variable in sequence:
          statements(s)
"""
"""
  * letter - variable
  * in - membership operator
  # we are using 'string' here
"""
print("\nString Iteration")

for letter in "python":
    print("character is", letter)

# Iterating over a list 
print("\nList Iteration") 
list_A = [10,20,30] 
for i in list_A: 
    print(i)

# In for loop,we can also use '_' in the place of condition/sequence
_ = [10,20,30]
for i in _: 
    print(i)

#Function calls

#pass -NOP
print("\nPass")
"""
     We use pass statement to write empty loops.
"""
a = 0
while(a<10):  #outer loop
    if(a==3):  #inner loop
        pass
    print(a)
    a= a+1

#break - It brings control out of the loop from inner-most loop
print("\nbreak")

a = 0
while(a<10):  #outer loop
    if(a==3):  #inner loop
        break
    print(a)
    a= a+1

#continue - It returns the control to the beginning of the loop.
print("\ncontinue")


a = 0
while a < 10:
    a =a + 1
    if a == 3:
        continue
    print(a)
    
print('Loop ended.')

    




   
