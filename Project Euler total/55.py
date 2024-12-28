
def reverse(number):
    numstr = str(number)
    newstr = []

    for i in range (len(numstr)):
        newstr.append(numstr[int(len(numstr))-i-1])

    newstr = int("".join([str(num) for num in newstr]))
    return newstr

def isPalidromic(number):
    numstr = str(number)
    
    for i in range (int(len(numstr) / 2)):

        if numstr[i] != numstr[-i-1]:
            return False
        
    return True

def checkLychrel(number):
    lych = number + reverse(number)

    for i in range (49):
        if isPalidromic(lych) == True:
            return True
        lych += reverse(lych)

    return False

sum = 0
for i in range (1,10_000):

    if checkLychrel(i) == True:
        sum += i

print(sum)