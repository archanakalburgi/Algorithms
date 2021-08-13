'''
i/p = [0,1,0,1,0]
o/p = [4,2,2,4]
'''

def cost(array): # t: O(n^2) s: O(n)
    result = [0]*(len(array)-1)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] == 1:
                result[i] += abs(j-i)
    return result

# print(cost([0,1,0,1,0]))