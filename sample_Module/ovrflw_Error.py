#OverflowError - math range error in Python
"""
   **indicates that an arithmetic operation has exceeded the limits of the current Python runtime.
   **In this script error is raised typically due to excessively large Float values,
       as Integer values that are too big.
"""

import math
answer=math.exp(1000)
print(answer)
