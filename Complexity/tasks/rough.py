def compare(A, B):
    if A[0] == B[0]:
        return
    else :
        return compare(A[1:],B[1:])
    
def divide(array):
    if len(array) == 1 :
        return array
    else :
        mid = len(array)//2
        left = divide(array[:mid])
        right = divide(array[mid:])
        duplicate = compare(left,right)
        return duplicate 

'''
array = [1,2,3,4,4,5]
left = [1,2,3]
left = [1]
right = [2,3]

left = [2]
right = [3]


right = [4,4,5]
'''

print(divide([1,2,3,4,4,5])) 