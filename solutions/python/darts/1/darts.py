import math
def score(x, y):
    z1=1
    z2=5
    z3=10

    distance=math.sqrt(x**2+y**2)
    
    if distance<=z1:
        return 10
    if distance<=z2:
        return 5
    if distance<=z3:
        return 1
    else:
        return 0

