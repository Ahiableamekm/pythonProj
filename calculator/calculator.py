from art import logo
import os


def add(n1, n2):
    """Returns the sum of numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Returns result of subtraction"""
    return n1 - n2


def multiply(n1, n2):
    """Returns result of multiplcation"""
    return n1 * n2


def divide(n1, n2):
    """Returns result of multiplcation"""
    return n1 / n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}


def calculator():
    print(logo)
    on = True
    first_number = float(input("What is the first number?:"))

    while on:
        for symbol in operations:
            print(symbol)
        operation = input('pick an operation from above: ')
        next_number = float(input("What's the next number?: "))
        result = operations[operation](first_number, next_number)
        print(f'{first_number} {operation} {next_number} = {result}')
        
        should_continue = input(f"Type 'y' to continue with {result}, or Type n to start a new calculation:")
        if should_continue == 'y':
            first_number = result
        else:
            os.system('cls')
            calculator()


calculator()