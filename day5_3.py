#Adding all even numbers from 1 - 100

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

#Another method
total1 = 0
for number in range(2, 101, 2):
    total1 += number
print(total1)