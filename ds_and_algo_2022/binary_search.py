def binary_search(array, target):
    s = m = 0
    e = len(array)-1
    
    while s<=e:
        m = (s+e)//2
        if target == array[m]:
            return m
        if target > array[m]:
            s = m+1
        if target < array[m]:
            e = m-1
    return s

# assert(binary_search([1,6,8,12], 6))== 1
# assert(binary_search([10,20,30,40], 10))==0 
# assert(binary_search([],5)) == None
# assert(binary_search([1,22,34,43], 43)) == 3

# print(binary_search([1,6,8,12], 6)) # 1
# print(binary_search([1,22,34,43], 43)) # 3
# print(binary_search([10,20,30,40], 10)) # 0 
# print(binary_search([],5)) # None
# print(binary_search([1,22,34,43], 2)) # 3

print(binary_search([1,22,34,43], 54)) # 54


