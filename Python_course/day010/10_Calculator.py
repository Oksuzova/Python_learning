def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    num1 = float(input("What`s the first number?: "))
    for key in operations:
        print(key)
    restart = True

    while restart:
        operation_symbol = input("Please, pick the operation: ")
        num2 = float(input("What`s the next number?: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        if input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            restart = False
            calculation()

calculation()
