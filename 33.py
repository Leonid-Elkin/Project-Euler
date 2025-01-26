def check(numerator,denominator):
    actualsum = round(numerator/denominator,10)
    numeratorstr = str(numerator)
    denominatorstr = str(denominator)

    for digit in numeratorstr:
        if digit in denominatorstr:
            print(list(numeratorstr).pop(digit))
            if actualsum == round(int(list(numeratorstr).pop(digit))/int(list(denominatorstr).pop(digit),10)):
                return True
    return False

print(check(49,98))