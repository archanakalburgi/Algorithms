def find_last_position(array,n):
    start = 0
    end = len(array)
    while start<end:
        mid = (start+end) // 2
        if array[mid] <= n:  
            start = mid
        else:
            end = mid-1
    return start

print(find_last_position([1,2,2,2,5,6] , 2)) 