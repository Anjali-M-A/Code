#-----Error Task----

#non-default arg followed by dafault arg
  

def Func(a,b=1):
    return a+b
"""
  **SyntaxError: non-default argument follows default argument
  ** bcz we must make sure to not have a non-default argument after a default argument.
"""
