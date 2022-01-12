"""
helper(curr,prev):
    if curr == " ":
        return(int(curr), none)
    if curr in [+,-,*,/]
        return (int(prev),curr)
    else:
        return(int(str(prev)+str(curr)))

    

main():
    prev = none
    stack=s[i]
    op = {+,-,*,/}
    for i:
        new, operator = helper(str[i],prev)
        if operator == None:
            stack.append(new)
            prev=new 
        elif operator == "+":
            prev = new
            stack.append(new)
        elif operator == "-":
            s[i+1]=s[i+1]*-1
            stack.append(new)
            stack.append(s[i+1])
            i=i+1    
        elif operator == "*":
            last = stack.pop()
            res = last*new
            stack.append(res)
        elif operator == "/":
            last = stack.pop()
            res = last/new
            stack.append(res)
    return sum(stack)
""" 

def helper(curr,prev): # (3,none), (+,3), (1,none), (*, 1)
    if curr == " " and prev == " ":
        return(None,None)
    if curr == " " and prev:
        return(int(prev),None)
    if curr in {"+","-","*","/"}: # (+,3)
        return (int(prev),curr) # (int(3), +) | (int(1), *)
    else:
        if prev:
            return(int(str(prev)+str(curr))) # 
        else:
            return(int(curr), None) # (3, none)| (1, none)

def is_digit(s): # TODO
    pass

def calculator(string): # "3+1*2"
    stack = []
    prev = None
    i=0
    while i < len(string):
        number, operator = helper(string[i], prev) # (3,none) number=3, operator==None| (+,3) number = 3, op=+| (1,none) (1,none)
        # | (*,1) -> (int(1), *)
        print(f"num : {number}, operator : {operator},     stack : {stack},      prev : {prev}")
        if operator == None:
            prev = number       # prev=3 , prev=1
            # stack.append(number)
        if operator == "+": # num=3,op=+
            stack.append(number) # [3,1]
            prev = None
        if operator == "-":
            pass
        if operator == "*":
            last = int(stack.pop())
            res = last * int(string[i+1])
            stack.append(res)
            i = i+1
        if operator == "/":
            pass
        i+=1
    print(stack, sum(stack))
    return "End"

print(calculator("3+1*2"))
