# [2,3,4,5]
def maximum_elelment(array):
    temp = 0
    temp2 = 0
    for i in range(0, len(array)):
        if temp < array[i]:        
            temp = array[i]
    array.remove(temp) 
    for j in range(0, len(array)):
        if temp2< array[j]:
            temp2 = array[j]

    return temp,temp2  
            
print(maximum_elelment([22,2,3,4,5,10])) 


'''
time complexity will be 
n + (n-1)= 2n -1 
ignoring constants 

as n increases the time taken will also increase 

linear growth 
''' 