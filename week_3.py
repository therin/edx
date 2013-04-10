def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)    
def f1(x):
    import math
    return 60*math.e**(math.log(0.5)/55.6 * x)

def radiationExposure(start, stop, step):
    sum = 0
    while (start < stop):
        sum = sum + f(start) * step
        start = start + step
    return sum

print radiationExposure(0, 5, 1)
print radiationExposure(40,100,1.5)
print radiationExposure(600, 1200, 5)