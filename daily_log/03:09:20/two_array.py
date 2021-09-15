'''
write a program which takes two sorted arrays and gives back a new array containing elements 
that are present in both of the input arrays. 
And there should not be any duplicates - 

input ->  [2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10] 
output -> [5,6,8]
'''

'''
two arrays
arrays are sorted 

new array -> common elements 
'''

def common_elements_array1(A, B):
    C = []
    for i in A:
        if i in B :
            C.append(i) 
    return list(set(C)) 

'''
time complexity = n^2  
''' 

def binary_search(array,key):
        start = 0
        end = len(array)-1
        while start <= end:
            mid = (start + end)//2
            if key < array[mid]:
                end = mid - 1 
            elif key > array[mid] :
                start = mid + 1 
            else :
                return mid   
            
        return None


def common_elements_array2(A,B):
    C = [] 
    if len(A) == 0:
        return []
    elif len(B) == 0:
        return []
    else:
        for i in A:
            res = binary_search(B,i)
            if res:
                result = binary_search(C,i)
                if result == None:
                    C.append(i) 
            # if res and i not in C:
            #     C.append(i) 
    return C 

'''
n log n + n log n + n log n ..... (n times) = n log n 
- callot do it without using for loop 
'''


# def common_elements_array3(A, B):
#     c = []
#     if len(A) == 0 or len(B) == 0 :
#         return None
#     else :
#         binary_search(B, A[i])

print(common_elements_array2([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10]))  