'''
problem : find the sum of list of 10 elements(numbers) 
'''

'''
i/p : [10,20,30,40,50,60,70,80,90,100]
o/p : 550
'''

'''
steps :
1. create a list of size 10
2. create sum = 0
3. iterate through list (through for loop)
4. keep adding elements as you iterate (accumulate variable sum) 
5. print sum 
'''

def sum_for_loop(input_list):
    sum = 0 
    count = 0
    for element in input_list:
        sum = sum + element
        count = count + 1
    return sum, count

input_list = [10,20,30,40,50,60,70,80,90,100]
print(sum_for_loop(input_list)) # no of steps = 39 (without count = 28)

# Recursion

# [1] = 1 
# [1, 2] = 3 
# [1,2,3] = 3 + 3 = 6
# [1,2,3,4] = 6 + 4 = 10 
#  1 + 2 
#  (2 + 1 ) + 3 = 2 +( 3 + 1)

# 0
# 10, sum = 10 
# 20 sum = sum + 20


# [1,2]  3
def sum_tail_recursion(intlist, sum = 0, count = 0): #tail recursive
    count = count + 1
    if intlist:
        sum = sum + intlist[0]
        return (sum_tail_recursion(intlist[1:], sum, count)) 
    else:
        return sum, count  

print(sum_tail_recursion([1,2,3,4,5,6,7,8,9,10]))  # no of steps 67 (without count = 56)



# input = [1,2,3]
def sum_normal_recursion(inputlist, count = 0): #normal recursion 
    count = count + 1  
    if inputlist:
        fst_eml = inputlist[0] # frt = 1, 
        return (fst_eml + sum_normal_recursion(inputlist[1:], count))  
    else:
        return 0     

print(sum_normal_recursion([1,2,3])) # no of steps = 25 (without count = 21) 







