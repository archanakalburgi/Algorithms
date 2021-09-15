def element_original_index(array, key):
    index_array = list(range(len(array)))
    if key in array : 
        count = array.count(key)
        indices = [] 
        if count > 1:
            for i in range(0,count): 
                index = array.index(key) 
                indices.append(index)
                array[index] = ''
            return indices  
        else :
            return array.index(key)
    else :
        return 'Element not present' 

print(element_original_index([4,3,6,1,0,3,3],3)) 

# print(element_original_index([4,3,6,1,0],5) ) 






'''
1st trial :
    let's remove the key and check if the key is present again in the array 
    remove - it removes the element encountered the first time 

first approach is confusing and keeping track becomes difficult 

2nd trial :
    try to get the no of time the key is repeating in the input array 

    then ??

3rd:
    - trying to avoid one more for loop to get the count of the repeation 

    easy way to get how many times a element is repeating in an array : is by count method 
    (internet)

    - same index is getting apended again and again as the array dosn't change 
        
        so remove the key 1st time when found 

        but this will change the positioning of the elements hence the array and so the wrong 
        index will be returned 

    - instead removing replace the 1st key with an empty element this wn't change the indexing of the 
    remaining element

        how : replace method ?
'''
