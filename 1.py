sum = 0

for number in range(1000):
    if number % 3 or number % 5 == 0:
        sum += number

print(sum)