# Calculator with dictionary


def add(num1, num2):
    """A function that adds two or more variables"""
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    num1 = float(input("Enter the first number: "))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    for operator in operations:
        print(operator)

    end_of_calc = False
    while not end_of_calc:
        operator_input = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        selected_operator = operations[operator_input]
        result = selected_operator(num1, num2)
        print(f"{num1} {operator_input} {num2} = {result}")

        calc_continue = input("Type 'y' to continue with this result or type 'n' to start a new calculation: ")
        if calc_continue == "y":
            num1 = result
        else:
            end_of_calc = True
            calculator()


calculator()
