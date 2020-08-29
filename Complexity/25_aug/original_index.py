from binary_search import binary_search 
def element_original_index(array, key):
    '''
    input
    array = [4,6,1,0,3]
    key = 3

    output 
    index of 3 in array 
    -> 4 
    '''
    index_array = list(range(len(array)))
    index = array.index(key)
    status = binary_search(array,key)
    if status :
        return index 

print(element_original_index([4,6,1,0],0)) 