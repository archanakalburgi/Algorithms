'''
mergeSort(inputArray)
for i in nums :
    binay_search (array, i) 
if found :
    return True 
'''




def merge(a,b):
    if len(a) == 0 and len(b) == 0:
        return []
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a 
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:],b)
    if b[0] <= a[0]:
        return [b[0]] + merge(a, b[1:])

def merge_sort(array):
    if len(array) == 1:
        return array 
    
    else :
        mid = len(array)//2

        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:]) 

        return merge(left,right)


def binary_search(sortedArray, key):
    mid = len(sortedArray) // 2
    
    if len(sortedArray) >= 1:

        if key == sortedArray[mid] :
            return True

        if key < sortedArray[mid] :
            return binary_search(sortedArray[0 : mid], key)  
    
        if key > sortedArray[mid] :
            return binary_search(sortedArray[mid+1 : len(sortedArray)],key) 
      
    return False 


def duplicateElements(nums):
    '''
    i/p -> [4,5,2,4] -> list
    o/p -> true -> bool 
    '''
    sortedArray = merge_sort(nums) 
    for n in nums:
        res = binary_search(sortedArray, n)
        if res :
            return True 
        else :
            return False 

print(duplicateElements([3,6,3,1])) 

'''
modify merge algorithm to take care of the duplicates 
'''