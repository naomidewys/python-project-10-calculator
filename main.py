import art

# Define the operations as functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Create operations dictionary
operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Create calculator function
def calculator():
    # Add title and logo so it appears each new session
    print(art.logo)
    print("Welcome to the Python Calculator")

    # Set condition for while loop to keep running
    continue_calculating = True

    #First question separate from while loop so each total can be used in each subsequent calculation
    n1 = float(input("What's the first number? "))

    while continue_calculating:
        print("+   -   *   / ")
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number? "))
        total = operations_dict[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {total}")

        more_calculations = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()

        if more_calculations == 'y':
            n1 = total
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()

calculator()