from history import History
from scientific import power, square_root, factorial

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


if __name__ == "__main__":
    calc_history = History()

    print("=== Ultimate Calculator ===")


    result = add(10, 5)
    calc_history.add_record("+", 10, 5, result)


    result = power(2, 8)
    calc_history.add_record("^", 2, 8, result)

    result = square_root(144)
    calc_history.add_record("√", 144, 0, result)

    result = factorial(5)
    calc_history.add_record("!", 5, 0, result)

    calc_history.show_history()