
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

def isNumber(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def infixToPostfix(tokens):
    result = []
    op_stack = []
    
    for token in tokens:
        if isNumber(token):
            result.append(float(token))
        elif token in ops.keys():
            while (op_stack and 
                   priority[op_stack[-1]] >= priority[token]):
                result.append(op_stack.pop())
            op_stack.append(token)
        else:
            raise ValueError()
    
    while op_stack:
        result.append(op_stack.pop())
    
    return result

def calculatePostfix(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ops.keys():
            if len(stack) < 2:
                raise ValueError()
            b = stack.pop()
            a = stack.pop()
            result = ops[token](a, b)
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError()
    return stack[0]

def main():
    try:
        user_input = input("input expression: ").split()
        postfix_tokens = infixToPostfix(user_input)
        result = calculatePostfix(postfix_tokens)
        print(f"Result: {result}")
    except ValueError:
        print(f"Invalid input.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(e)
    except EOFError:
        return
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()