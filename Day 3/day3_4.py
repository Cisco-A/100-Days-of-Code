#A pizza ordering system

#Initialization
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Prizes
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# pepperoni_for_small = 2
# pepperoni_for_medium_or_large = 3
# extra_cheese_for_any = 1

#Flow control



# if size == 'S':
#     if add_pepperoni == 'Y':
#         small_pizza += 2
#     if extra_cheese == 'Y':
#         small_pizza +=1
#     print(f'Your bill is ${small_pizza} ')  
# else:
#     print(f'Your bill is ${small_pizza}')


# if size == 'M':
#     if add_pepperoni == 'Y':
#         medium_pizza += 3
#     if extra_cheese == 'Y':
#         medium_pizza +=1
#     print(f'Your bill is ${medium_pizza} ')  
# else:
#     print(f'Your bill is ${medium_pizza}')


# if size == 'L':
#     if add_pepperoni == 'Y':
#         large_pizza += 3
#     if extra_cheese == 'Y':
#         large_pizza +=1
#     print(f'Your bill is ${large_pizza} ')  
# else:
#     print(f'Your bill is ${large_pizza}')

#The above code was in the wrong format(you can try to make that format work later, if possible)


#Correct format

#Declare a global bill variable

bill = 0

#Flow Control

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have made an invalid entry. Use upper case if you did not.")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is $ {bill}")