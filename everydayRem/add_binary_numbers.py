# binary addition
def isBinary(string):
    for s in string:
        if s not in ['0','1']:
            return False
    else:
        return True 
        
def binaryToDecimal(string):
    num = [] 
    reverseString = string[::-1]
    for i in range(len(string)):
        num.append(int(reverseString[i])*pow(2,i)) 
    return sum(num) 

def bin_add(a, b):
    if a and b and isBinary(a) and isBinary(b):
        number = binaryToDecimal(a) + binaryToDecimal(b)
        return bin(number)[2:]
    else:
        return None 
    
def addBinaryNumbers(a, b):
    if a != "" and b != "":
        for ca in a:
            if ca != '0'and ca != '1':
                return None
        for ba in b:
            if ba != '0'and ba != '1':
                return None
        return bin(int(a, 2)+int(b, 2))[2:]
    else:
        return None

print(bin_add("1010", "1011")) 
print(addBinaryNumbers("1010", "1011")) 