def numPens(n):
   
    if n == 0:
        return True
    for i in (5, 8, 24):
        if n >= i and numPens(n - i):
            return True
    return False