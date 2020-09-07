def merge(A,B):

    C = []
    i = 0
    j = 0
    
    while i <= len(A)-1 and j <= len(B)-1 :
        if A[i] < B[j] :
            C.append(A[i])
            i+=1
        
        else:
            C.append(B[j])
            j+=1
    
    C.extend(A[i:])
    C.extend(B[j:])
    
    return C 

def merge_sort(array) :
    if len(array) <= 1:
        return array 
    else : 
        mid = int((len(array)) / 2)  
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        sorted_array = merge(left_array, right_array) 

# print(merge_sort([[1,3],[2,5],[3,8]])) 
print(merge_sort([1,2,3,4,2,6,4]))  