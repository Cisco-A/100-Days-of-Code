# Popular interview problem
# The Fizzbuzz game

for number in range(1, 101):
    if number % 15 == 0:
        number = "Fizzbuzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"

    print(number)
