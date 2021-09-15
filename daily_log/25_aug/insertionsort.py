def insertion_sort(array):
    for i in range(1,len(array)):
        j = i-1
        key = array[i] 

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        
        array[j+1] = key 
    return array 

# print(insertion_sort([9,8,7,6,5,4])) 