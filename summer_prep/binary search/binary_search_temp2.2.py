'''
Find the first position of n in a given sorted array of integers. 

Example 1:
    input: n=2, array=[1,2,2,2,5,6]
    output: 3

    the last position 3 is present is at 3rd position
'''

def find_last_position(n, array):
    start = 0
    end = len(array)
    while start<end:
        mid = (start+end)//2
        if array[mid] <= n:
            start=mid
        else:
            end = mid-1
    return start

n = 2
array = [0,1,1,1,2,6]
print(find_last_position(n, array))