digit1 = int(input("Enter the first digit: "))
digit2 = int(input("Enter the second digit: "))
oprator = input("Enter operator: ")

def calculator(digit1, digit2, oprator):
    if oprator == '+':
        return digit1 + digit2
    elif oprator == '-':
        return digit1 - digit2
    elif oprator == '*':
        return digit1 * digit2
    elif oprator == '%':
        return digit1 % digit2
    elif oprator == '**' :
        return digit1 ** digit2
    elif oprator == '//' :
        return digit1 // digit2
    try :
        if oprator == '/' :
            return digit1 / digit2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    else :
        return "Enter valid input"
print(calculator(digit1, digit2, oprator))