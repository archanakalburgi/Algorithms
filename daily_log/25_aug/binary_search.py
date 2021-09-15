import mergesort 
from insertionsort import insertion_sort 

def binary_search(array, key):
    '''
    [4,1,5,2,8,0]
    1. sort the array 
    2. divide array into 2 equal parts -< left_array, right_array 
    3. if key < mid :
        don't look for key here
    4. if key > mid
        look for key here 
    '''
    mid = int(len(array)/2) 
    index = array.index(key)
    if len(array) >=1:
        if key == array[mid] :
            # return sorted_array[mid]  
            return True
        
        if key < array[mid] :
            return binary_search(array[0 : mid], key) 

        if key > array[mid] :
            return binary_search(array[mid+1 : len(array)], key) 

    return False 

print(binary_search(mergesort.merge_sort([4,1,5,2,8,0]),8))  
 

