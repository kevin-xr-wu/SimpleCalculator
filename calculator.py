import re

def add(x, y):
    try:
        return int(x) + int(y)
    except ValueError:
        return float(x) + float(y)

def subtract(x, y):
    try:
        return int(x) - int(y)
    except ValueError:
        return float(x) - float(y)

def multiply(x, y):
    try:
        return int(x) * int(y)
    except ValueError:
        return float(x) * float(y)

def divide(x, y):
    try:
        return int(x) / int(y)
    except ValueError:
        return float(x) / float(y)

print("Welcome to my simple calculator!")
print("Please enter a calculation:")

while True:
    expression = input()
    operator_stack = []
    postfix_expression = []
    line = []
    number = ""
    for token in str(expression):
        if token == "-" and number == "":
            number += token
            continue

        if token == "+" or token == "*" or token == "/" or token == "-" or token == "(" or token == ")":
            if number != "":
                line.append(number)
            line.append(token)
            number = ""
        else:
            number += token

    if number != "":
        line.append(number)

    print(line)

    for token in line:
        try:
            operand = float(token)
            postfix_expression.append(token)
        except ValueError:
            if operator_stack:
                top = operator_stack.pop(0)
                operator_stack = [top] + operator_stack
                if top == "(":
                    operator_stack = [token] + operator_stack
                else:
                    if token == "(":
                        operator_stack = [token] + operator_stack
                    elif token == ")":
                        op_top = operator_stack.pop(0)
                        while op_top != "(":
                            postfix_expression.append(op_top)
                            op_top = operator_stack.pop(0)
                    elif token == "*" or token == "/":
                        op_top = operator_stack.pop(0)
                        # postfix_expression.append(op_top)
                        if op_top == "+" or op_top == "-":
                            operator_stack = [op_top] + operator_stack
                            operator_stack = [token] + operator_stack
                        elif op_top == "*" or op_top == "/":
                            postfix_expression.append(op_top)
                            operator_stack = [token] + operator_stack
                    elif token == "+" or token == "-":
                        # used to check
                        op_top = operator_stack.pop(0)
                        if op_top == "+" or op_top == "-":
                            postfix_expression.append(op_top)
                            operator_stack = [token] + operator_stack
                        elif op_top == "*" or op_top == "/":
                            postfix_expression.append(op_top)
                            # test with next top
                            while operator_stack:
                                p_top = operator_stack.pop(0)
                                if op_top == "+" or op_top == "-":
                                    postfix_expression.append(p_top)
                                    operator_stack = [token] + operator_stack
                                elif op_top == "*" or op_top == "/":
                                    postfix_expression.append(p_top)
                            # postfix_expression.append(token)
                            operator_stack = [token] + operator_stack
            else:  # stack is empty
                operator_stack = [token] + operator_stack

    for operator in operator_stack:
        postfix_expression.append(operator)

    print(postfix_expression)

    postfix_stack = []
    for token in postfix_expression:
        if token == "quit":
            exit(0)
        if token == "+":
            x = postfix_stack.pop()
            y = postfix_stack.pop()
            a = add(x, y)
            postfix_stack = [a] + postfix_stack
        elif token == "-":
            x = postfix_stack.pop()
            y = postfix_stack.pop()
            a = subtract(y, x)
            postfix_stack = [a] + postfix_stack
        elif token == "*":
            x = postfix_stack.pop()
            y = postfix_stack.pop()
            a = multiply(x, y)
            postfix_stack = [a] + postfix_stack
        elif token == "/":
            x = postfix_stack.pop()
            y = postfix_stack.pop()
            a = divide(y, x)
            postfix_stack = [a] + postfix_stack
        else:
            postfix_stack.append(token)

    print("Result is " + str(postfix_stack.pop()))

print("Still implementing!")