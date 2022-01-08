"""
i/p : a = [1,2,3,4,5]
b = [1,5,2,4,3]

t/f : 
    t -> b is strictly ascending  
    f
"""


def solution(a):
    result = list()

    mid = len(a)//2
    a1 = a[0: mid]
    a2 = a[mid: len(a)]
    
    last = len(a2)-1

    for i in range(len(a1)):
        result.append(a1[i])
        result.append(a2[last])
        last = last-1
    
    if len(a)%2!=0:
        result.append(a2[0])

    for i in range(1,len(result)-1):
        if result[i]>result[i-1]:
            return False
    
    return True



a = [-91,-84,-67,-44, 9, 70, 88, 37,-11,-67,-72,-87] # false
print(solution(a)) 