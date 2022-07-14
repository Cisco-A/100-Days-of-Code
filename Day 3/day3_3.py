# Getting leap years

year = int(input("Which year do you want to check? "))

# Every year that is evenly divisible by 4 is a leap year
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

parameter_1 = year % 4
parameter_2 = year % 100
parameter_3 = year % 400

# Flow Control

if parameter_1 == 0:

    if parameter_2 != 0:
        print("This is a leap year.")
    elif parameter_2 == 0:
        if parameter_3 == 0:
            print("This year is a leap year")
        else:
            print("This year is not a leap year.")

else:
    print("This year is not a leap year")
