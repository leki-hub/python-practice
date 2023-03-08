#A simple calcilator
#The "while True" statement in the above calculator code creates an infinite loop.The loop will continue to execute as long as the condition "True" is true, which is always the case.The loop will only exit when the program encounters a "break" statement. 
def calculator():
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation. Please enter a valid operation.")
            continue
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:
            result = num1 / num2
            
        print("Result:", result)
        repeat = input("Do you want to perform another operation?  : Yes/NO)")
        if repeat != "Yes":
            break # We use break to stop the iteration. Ie , Whenever a program encounters break, it stops.32
calculator()
