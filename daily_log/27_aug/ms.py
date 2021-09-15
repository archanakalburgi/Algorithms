def merge_recursive(A, B):

    if len(A) == 0 and len(B) == 0:
        return [] 
    
    else :
        if len(B) == 0:
            return A 
        
        elif len(A) == 0:
            return B
        
        else :
            if A[0] < B[0] :
                return [A[0]]+ merge_recursive(A[1:], B)
            
            else :
                return [B[0]]+ merge_recursive(A,B[1:])

def merge_sort(array) :
    if len(array) == 1:
        return array 
    else : 
        mid = int((len(array)) / 2)  
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        sorted_array = merge_recursive(left_array, right_array) 
        return sorted_array 
 