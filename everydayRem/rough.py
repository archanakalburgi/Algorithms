# def one_plus(array):
#     increment = 1 
#     for i in reversed(range(len(array))):
#         last = (array[i] + increment) % 10 
#         if last < array[i]:
#             increment = 1 
#         else:
#             increment = 0
#         array[i] = last
#     if increment == 1:
#         return [1] + array
#     return array 

# def romanNumbers(string):
#     Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     number = 0

#     for i in range(len(string)-1):
#         first = string[i] 
#         second = string[i+1]

#         if Roman_number[first] > Roman_number[second]:
#             number += Roman_number[first] 
#         else:
#             number -= Roman_number[second]

#     number += Roman_number[string[-1]]

#     return number

# print(romanNumbers("XI"))

# def binary_addition(a,b):
#     if a != "" and b != "":
#         for ca in a:
#             if ca != "0" and ca != "1":
#                 return None 
#         for cb in b:
#             if cb != "0" and cb != "1":
#                 return None 
#         return bin(int(a,2)+int(b,2))[2:]
#     else:
#         return None 

# print(binary_addition("10", "01"))

print("\n")
# 1 -> a 
F = lambda seq: (seq[i:] + seq[:i]
for i in range(len(seq)))
list(F([1, 2, 3]))
for x in F((1, 2, 3)):
    print(x, end=' ')

print("\n")
# 2 -> c
def z (f, seq):
    val = seq [0]
    for next_val in seq [ 1: ]:
        val = f(val, next_val)

    return val

print(z(lambda x , y : x + y , [ 1 , 8 , 3 , 7 ] )) 

print("\n")
# 3 -> b
# permute2 -> given in class 
def permute2(seq):
    if not seq:   # Shuffle any sequence: generator
        yield seq # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]   # Delete current node
            for x in permute2(rest):     # Permute the others
                yield seq[i:i+1] + x     # Add node at front

# print(list(permute2('123')))

for x in permute2('123'):
    print(x, end=' ')
print("\n")