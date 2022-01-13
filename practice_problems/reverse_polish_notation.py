def is_number(s):
    try:
        float(s)
        return True
    except Exception:
        raise Exception

def add (value1, value2) :
    return value1+value2

def substract (value1, value2) :
    return value2-value1

def multiply (value1, value2) : 
    return value1*value2

def divide(value1, value2) :
    try:
        return value2/value1 #-2, 4-> 4/2
    except Exception:
        raise Exception

# ['4', '2']
def rpn(inputs):
    stack = list()
    operators = {"+": add, "-": substract, "*": multiply, "/":divide}
    for token in inputs:
        if token in operators: # N4 N
            try:
                value1 = float(stack.pop()) #
                value2 = float(stack.pop())
                if is_number(value1) and is_number(value2) :
                    result = operators[token](value1, value2) # divide(-2, 4)
                    stack.append(result)
            except Exception:
                raise Exception
        else:
            stack.append(token)
    return stack.pop() 

inputs = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(rpn(inputs))