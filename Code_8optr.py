#Operator Types
"""
   ** Arithmetic
        symbols - +, -, *, /, //, %, **(power)

   ** Logical
        symbols - and, or, not

   ** Assignment
        symbols - =, +=, -=, *=, /=, //=, %=, **=, &=, ^=, |=

   ** Comparison
        symbols - ==, !=, <, >, <=, >=, <>

   **Bitwise
        symbols - &, |, ^, ~, <<, >>

   ** Unary
        symbols - @+, @-
        
   ** Identity
        symbols - is, is not

   ** Membership
        symbols - in, not in


 *** Additional Topics
        - Precedence
        - Associativity
"""

#Ternary Operator
"""
     * Used to select one of the two values based on a condition.
     * Expression to avoid multi-line if conditions
"""     
# Nested Ternary Operator
a, b, c = 15, 25, 22

max = "a is greater" if a > b and a>c else "b is greater" if b>c else "c is greater"

print(max)


# Arithmetic Operator
"""
    Exceptional Cases:
      - string cannot be concatenated with int
      - but string can be multiplied with numeric value (only int)
"""
  
a = 9
b = 4
  
# Addition of numbers  
add = a + b  
  
# Subtraction of numbers  
sub = a - b  
  
# Multiplication of number  
mul = a * b  
  
# Division(float) of number  
div1 = a / b  
  
# Division(floor) of number  
div2 = a // b  
  
# Modulo of both number  
mod = a % b  
  
# Power 
p = a ** b

""" Exceptional Cases"""

#string can be multiplied with numeric value
string = "Anjali" * 3

sample = "2" + "Anjali"

#step_1= "anjali" + 3  - TypeError: can only concatenate str (not "int") to str
#step_2 = "anjali" * 3.2 - TypeError: can't multiply sequence by non-int of type 'float'
#step_3= "anjali" * "3" - TypeError: can't multiply sequence by non-int of type 'str'
  
# print results  
print(add)  
print(sub)  
print(mul)  
print(div1)  
print(div2)  
print(mod) 
print(p)
print(string)
print(sample)

#Program to demonstrate '/'(division) and '//'(floor division) are different.
"""
    * In Python 3, ‘/’ division operator does floating point division for both int and float arguments
    * floor division operator is “//” returns floor value for both integer and floating point arguments
"""    

# A program to demonstrate use of "/" for both integers and floating points.
print (5/2)
print (-5/2)
print (5.0/2)
print (-5.0/2)

print("\r")  

# A program to demonstrate use of "//" for both integers and floating points #it returns  only the floor value
print (5//2)
print (-5//2)
print (5.0//2)
print (-5.0//2)

# Exponent operator ** has right-to-left order in Python.

# Shows the right-left order of **
# Output: 512, Since 2**(3**2) = 2**9
print(2 ** 3 ** 2)

"""#We can see that 2 ** 3 ** 2 is equivalent to 2 ** (3 ** 2)"""

#Logical Operators
"""
 Logical operators perform Logical AND, Logical OR and Logical NOT operations
"""   
print(True and True)

print(True and False)
  
print(False and True)

print(False and False)

print(True or False)
   
print(not True)

print(not False)

print(not 2)
 
print(not 0)

print(False == 0)

print(4 and 0)

print(3 and 3)

# Assignment Operator/Conditional Operator

a = 4
c = 0

c += a
print ("Value of c is ", c )

c *= a
print ("Value of c is ", c )

c /= a 
print ("Value of c is ", c )

c = 2
c %= a
print ("Value of c is ", c)

c **= a
print ("Value of c is ", c)

c //= a
print ("Value of c is ", c)

print(1<3)
print(1>-1)
print(1<=2)
print(3>=2)
print(3<=2)

print("\r")

#Comparison/Relational Operator

a = 4
b = 6
  
# a > b is False 
print(a > b) 
  
# a < b is True 
print(a < b) 
  
# a == b is False 
print(a == b) 
  
# a != b is True 
print(a != b) 
  
# a >= b is False 
print(a >= b) 
  
# a <= b is True 
print(a <= b)

"""
  **Exceptional Cases:
     1. TypeError: '>=' not supported between instances of 'int' and 'str'    
com = 1 >= "anju"
print(com)

     2. '<>' means 'Not Equals to'.
     It works exactly the same as the operator '!= ' does
print(a<>b) #SyntaxError : invalid syntax
print((1!=) and (1<>)) #SyntaxError : invalid syntax
"""
#Bitwise Operation
"""
  ** Bitwise operators acts on bits and performs bit by bit operation
"""
a = 10
b = 4
  
# bitwise AND operation   
print(a & b) 
  
# bitwise OR operation 
print(a | b) 
  
# bitwise NOT operation  
print(~a) 
  
# bitwise XOR operation  
print(a ^ b) 
  
# bitwise right shift operation  
print(a >> 2)
print(a >> 3)
  
# bitwise left shift operation  
print(a << 2)
"""
  Exception Cases:
   ** a = b'1010'
      a>>2 
    #TypeError: unsupported operand type(s) for >>: 'bytes' and 'int'

   ** a >> (b'0010) 
     #TypeError: unsupported operand type(s) for >>: 'bytes' and 'bytes'
"""
#Unary Operator
"""
  Exceptional Cases:
  ** @+ and @- -SyntaxError : invalid syntax
"""
print(+4)
print(-4)

#Identity Operator

   #is  - True if the operands are identical 
   #is not - True if the operands are not identical 

"""
  #Exceptional Cases:
   ** is
     SyntaxError: invalid syntax
   ** is not
      SyntaxError: invali syntax
"""      
a1 = 3
b1 = 3
str_1 = 'AnjaliAnnappa'
str_2 = 'AnjaliAnnappa'
list_A = [1,2,3] 
list_B = [1,2,3] 
  
print(a1 is b1)  
print(a1 is not b1)

#memory allocation
print(id(a1))
print(id(b1))
  
print(str_1 is list_B) 
  
# Output is False, since lists are mutable. 
print(list_A is list_B)

# Membership Operator
    #in - True if value is found in the sequence
    #not in - True if value is not found in the sequence

list_1 = [1,2,3]

print(1 in list_1)

print(1 not in list_1)

print("1" in list_1)

list_2 = ["1",2,3]
print("1" in list_2)


  




        
           

         
