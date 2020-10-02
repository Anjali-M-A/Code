#-------Error Task------

#non-keyword arguments are followed by keyword arguments
def add(a,b):
    print(a+b)
add(a=2,'3')
"""
  **SyntaxError: non-keyword arg after keyword arg
  **bcz Having a positional argument after keyword arguments will result in errors.
"""
