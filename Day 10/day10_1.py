# Days in months


def is_leap(year):
    parameter_1 = year % 4
    parameter_2 = year % 100
    parameter_3 = year % 400

    if parameter_1 == 0:

        if parameter_2 != 0:
            return True
        elif parameter_2 == 0:
            if parameter_3 == 0:
                return True
            else:
                return False

    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_the_month = month_days[month - 1]

    for day in range(len(month_days)):
        if is_leap(year):
            if day_of_the_month == 28:
                return 29
            else:
                return day_of_the_month
        else:
            return day_of_the_month

    # As usual, I went bogus again with my code
    # Here is the straightforward part
    # Ignore the for loop and just start at the first indent

    # if is_leap(year) and month == 2:
    #     return 29
    # else:
    #     return day_of_the_month


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
