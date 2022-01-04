'''
Your task to check whether it is possible to construct a given array of integers from a bunch of given pieces.
More formally, you are given an array of distinct non-negative integers arr and an array of integer arrays pieces 
Your task is to check whether it is possible to arrange the arrays of
pieces in a such a way that they can be concatenated to form an array equal to arr
(containing all the same elements in the same order).

For arr = [1, 2, 5, 3] and pieces = [[5], [1, 2], [3]] the output should be solution(arr, pieces) = true
The arrays of pieces can be arranged in the order [1, 2] [5] and [3] , 
which would be equal to arr = [1, 2, 5, 3] when concatenated.

For arr = [1, 2, 5, 3, 6] and pieces = [[1, 2], [5], [6, 3]] , the output should be solution (arr, pieces) = false
'''

def check_seq_in_order(piece, arr):
    start = 0 
    end = len(piece)
    while end<=len(arr):
        if piece == arr[start:end]:
            return True
        else:
            start += 1
            end += 1
    return False

def solution(arr, pieces):
    for piece in pieces:
        if check_seq_in_order(piece, arr)==False:
            return False
    return True

def hashmap_solution(arr, pieces):
    '''
    hashmap of arr elements
    iterate pieces
        if len(piece) == 1
            piece[0] not in hashmap: return false 
        else
            iterate piece : 0-len(piece)
                if piece[i] not in hashmap : return false
                else 
                    if hashmap[piece[i]] > hashmap[piece[i+1]] : return false
        return true
    '''
    hashmap = dict()
    for i,num in enumerate(arr):
        hashmap[num] = i
    
    # print(hashmap)
    
    for piece in pieces: # [[1, 2], [5], [6, 3]]    [1, 2, 5, 3, 6]
        if len(piece) == 1:
            if piece[0] not in hashmap: 
                return False
        else:
            for i in range(len(piece)-1): # [1,2]
                if piece[i] not in hashmap or piece[i+1] not in hashmap: # 1,2
                    return False
                elif hashmap[piece[i]] > hashmap[piece[i+1]]: 
                    return False
    return True


arr = [1, 2, 5, 3] 
pieces = [[5], [1, 2], [3]]
print(solution(arr, pieces)) 

arr1 = [1, 2, 5, 3, 6]
pieces1 = [[1, 2], [5], [6, 3]]
# print(solution(arr1, pieces1))

print(hashmap_solution(arr, pieces)) 
# print(hashmap_solution(arr1, pieces1)) 