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

from  typing import List 
def comparatorList(a: List[int] , b: List[int]) -> bool :
    '''
    input a = [int , int ]
    '''
    return a[1] < b[1]

def comparatorInt(a: int  ,b: int ) -> bool:
    return a < b 

def comparatorTuple(a : tuple , b : tuple ) -> bool :
    return a[1] < b[1]

def merge(A,B, comp):

    i = 0
    j = 0
    C = [] 
    print(A)
    print(B)
    
    while i <= len(A)-1 and j <= len(B)-1 :
        # if A[i][1] < B[j][1] : # [8, 2] [3, 4]  A[i][0] = [8]
        if comp(A[i], B[j]):
            C.append(A[i])
            i+=1
        
        else:
            C.append(B[j]) 
            j+=1
    
    C.extend(A[i:])
    C.extend(B[j:])
    
    return C 


def merge_sort(array, comp) :
    if len(array) == 1:
        return array 
    else : 
        mid = int((len(array)) / 2)  
        left_array = merge_sort(array[:mid],comp)
        right_array = merge_sort(array[mid:],comp)
        sorted_array = merge(left_array, right_array, comp) 
        return sorted_array 

# array = [[8,1],[3,2],[2,4],[1,3]]
# array = [2,8,15,18,5,9,12,17,1]
array = [(8,1),(3,2),(2,4),(1,3)]
print(merge_sort(array, comparatorInt))   


