from math import sqrt

def isPrime(number):
    for factor in range (2,int(sqrt(number) + 1)):
        if number % factor == 0:
            return False
    return True

def checkifconc(ognum,testnum):
    numstr = str(ognum)
    teststr = str(testnum)

    for digit in numstr:
        if digit not in teststr:
            return False
    return True

def check(number,adder):

    for i in range (3):
        if isPrime(number) and checkifconc(ogdig,number):
            number = number + adder
        else:
            return False 
    return True
        


ogdig = 1487
adder = 3330
number = ogdig

