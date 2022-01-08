"""
array = []
[]

array = [1]
[1]

array = [1,2,3]
result = [0+1+2, 1+2+3, 2+3+0]
return = [3,6,5]

neighbors(index, array): -> 0, [1,2,3] , 1, [1,2,3], 2 [1,2,3]
    if index == 0:  # len(array) == 1? TODO 
        return [array[index], array[index+1]] -> [1,2]
    elif index == len(array)-1
        return [array[index-1],array[index]] # [2,3]
    else:
        return [array[index-1], array[index], array[index+1]] # [1,2,3]

solution(array): -> [1,2,3]
    if len(array) <= 1: 
        return array
    iterate : i, 0-len(array)
        result.append(sum(neighbors(i, array)))  -> 0, [1,2,3]
        # result [3], [3,6] ,  [3,6,5]
    return result 
"""

def neighbors(index, array):
    if index==0:
        return [array[index],array[index+1]]
    elif index == len(array)-1:
        return [array[index-1], array[index]]
    else:
        return [array[index-1],array[index],array[index+1]]

def solution(array):
    result = list()
    if len(array) <= 1:
        return array 
    for i in range(len(array)):
        result.append(sum(neighbors(i, array))) 
    
    return result

assert(solution([1,2,3])==[3,6,5]) 
assert(solution([1])==[1])
assert(solution([])==[]) 
print(solution([1,2,3]))