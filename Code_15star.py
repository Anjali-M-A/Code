# Script to demonstrate Stars '*' in Different Shapes

# Right Triangle Shape
print("Right Triangle Shape")

rows = 5

#we have to take range i.e, 1 to rows+1
for i in range(1,rows+1):
    
# '*i' is how many '*'we want in each row
# '* ' is to print spaces b/w stars
     print("* "*i)

# Left Triangle Shape
print("\nLeft Triangle Shape")

rows = 5


for i in range(1,rows+1):
# "_2_" space to print left triangle 
    print("  "*(rows-i) + "* "*i)
    

# Triangle Shape
print("\nTriangle Shape")
rows = 5

for i in range(1,rows+1):
# "_1"space to print Triangle 
    print(" "*(rows-i) + "* "*i)

# Ulta Triangle Shape
print("\nUlta Triangle Shape")

rows =5

for i in range(rows,0,-1): 
    print("  "*(rows-i) + "* "*i)









    










 



