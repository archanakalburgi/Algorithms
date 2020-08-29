import m_s 

def binary_search(array, key, index=0):

    mid = len(array)//2 

    sorted_array = m_s.merge_sort(array)

    if len(array) == 0:
        return False

    else : 
        if key == sorted_array[mid] :
            # return sorted_array[mid]  
            # index = index + array.index(key) 
            return array.index(key)+index
            
        if key < array[mid] :
            return binary_search(sorted_array[:mid], key, index) 

        if key > sorted_array[mid] :
            return binary_search(sorted_array[mid+1:], key, index+mid) 

array = [4,9,6,1,0,8,2]

print(binary_search(array,9))  
