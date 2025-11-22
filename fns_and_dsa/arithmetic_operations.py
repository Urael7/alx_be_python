def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.
    Handles division by zero by returning an error message.
    """
    operation = operation.lower().strip()

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: division by zero"
        return num1 / num2

    else:
        return "Error: invalid operation"
