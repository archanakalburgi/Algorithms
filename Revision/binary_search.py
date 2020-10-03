def merge(a,b):
    if len(a) == 0 and len(b) == 0:
        return []
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a 
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:],b)
    if b[0] < a[0]:
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

# print(merge_sort([6,3,8,2,9])) 

print(binary_search(merge_sort([6,3,4,2,9]), 1))   


