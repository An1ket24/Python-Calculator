from Day_10_art import logo as lg
import os 
def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide 
}


def calculator():
    print(lg)
    num1 = int(input("Enter First number :"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an Operation :")
        num2 = int(input("Enter Second number :"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' continue calculation with {answer}, or type 'n' to start a new calculation :") == "y":
            num1 = answer
        else:
            should_continue =False
            clear = lambda:os.system('clear')
            clear()
            calculator()

calculator()

        
    
    
