from sort import merge_sort 

def binary_search(array, key):
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

# print(binary_search([0,1,6,8,9,20,100,150,200],8))


def binary_search_iterative(array,key):
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
            
        return 'Element not present'

print(binary_search_iterative([3,4,6,8,10,8,17],8))  


'''both recursive and iterative method time complexity is n log n ..
correct ??'''