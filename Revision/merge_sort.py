def merge(a, b):
    if len(a) == 0 and len(b) == 0:
        return 

    if len(a) == 0:
        return b

    if len(b) == 0:
        return a 
    
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)

    else:
        return [b[0]] + merge(a, b[1:]) 


def merge_sort(array):
    if len(array) == 1:
        return array 

    else :
        mid = len(array)//2

        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:]) 
        
        sorted_array = merge(left, right)
        
        return sorted_array 

print(merge_sort([2,5,1,0])) 

