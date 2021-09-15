def merge(A, B):

    if len(A) == 0 and len(B) == 0:
        return [] 
    
    else :
        if len(B) == 0:
            return A 
        
        elif len(A) == 0:
            return B
        
        else :
            if A[0] < B[0] :
                return [A[0]]+ merge(A[1:], B)
            
            else :
                return [B[0]]+ merge(A,B[1:])
            
A = [2,8,15,18]
B = [5,9,12,17]
print(merge(A,B)) 

'''
Since C has to be initialised to empty everytime merge is called, at the end merge returns empty list 
'''
