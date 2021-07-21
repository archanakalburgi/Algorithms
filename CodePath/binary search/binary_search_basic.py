'''
Using binary search return True if a given value is present in a sorted array. 
Return False if the value is not present 
'''

def find_value(array, val):
    start = 0 
    end = len(array)-1 
    mid = (start+end)//2   
    while start <= end:
        if array[mid] == val:
            # return True
            return mid
        if val > array[mid]:
            start = mid+1
            mid = (start+end)//2
        if val < array[mid]:
            end = mid-1
            mid = (start+end)//2
    return "Not Found" 

print(find_value([10,11,12,13,14,15,16,17,18,19,20],12))