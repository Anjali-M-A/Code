# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.


"""import dis"""

def sample():

 number = int(input("Enter a number: "))
 remainder = number % 2
 if (remainder == 0):
   print(number,"is an even number")
 else:
   print(number,"is an odd number")

sample()
"""print(sample.__code__.co_code)
print(dis.opname[sample.__code__.co_code[2]])"""



"""if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))"""  


    



   
