import math

def pageCount(n, p):
    if n/2 >= p:
        return math.ceil((p-1)/2)
    elif n % 2 == 0 and p == n-1:
        return math.ceil((n-p)/2)
    else:
        return math.floor((n-p)/2)