'''
problem : create 3 list of random numbers of size 10,20 and 30. Return numbers less than 10 from these list 

i/p : [1,2,5,9,12,23,56,78,50,55]
o/p : 1,2,5,9 
'''

import random 
def random_list(size, count=0):
    ran_list = random.sample(range(1,50),size)
    print(ran_list)
    for i in ran_list:
        count = count+1
        if i<10:
            print(i)
    return count     

print('count = '+str(random_list(10))) # no of steps = 40 / 29
print('count = '+str(random_list(20))) # no of steps = 72 / 51
print('count = '+str(random_list(30))) # no od steps = 104 / 73
