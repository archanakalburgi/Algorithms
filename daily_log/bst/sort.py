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
            

def merge_tail_recursive(A,B, C=[]):
    
    if len(A) == 0 and len(B) == 0:
        return []

    if len(B) == 0:
        return C + A

    if len(A) == 0:
        return C + B

    else :
        if A[0] < B[0]:
            # C.append(A[0])
            return merge_tail_recursive (A[1:], B, C + [A[0]]) 

        else :
            # C.append(B[0]) 
            return merge_tail_recursive(A, B[1:], C + [B[0]]) 


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
    if len(array) == 1:
        return array 
    else : 
        mid = int((len(array)) / 2)  
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        sorted_array = merge(left_array, right_array) 
        return sorted_array 