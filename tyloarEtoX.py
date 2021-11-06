import math
def factorial(num):
    total = 1
    for i in range(1,num + 1):
        total = i * total
    return total

def getEFor1(accuracy = 10):
    e = 0
    for i in range(accuracy):
        e += (1/ factorial(i))
    return e

def calcE(around = 0, acuurecy = 6, x = 0):
    e = 0
    eValue = getEFor1(accuracy=10)
    for i in range(acuurecy):
        power = math.pow((x - around), i)
        value =   power * math.pow(eValue, around) / factorial(i)
        e += value
    return e

# series from 3 around x = 2
print(calcE(around=3,acuurecy=10 , x=2))


# series form 0 at x = 2
print(calcE(around=0,acuurecy=10 , x=2))