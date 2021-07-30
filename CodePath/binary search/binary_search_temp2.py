'''
Find the first position of n in a given sorted array of integers. 

Example 1:
    input: n=2, array=[1,2,2,2,5,6]
    output: 1

    the first position 2 is present is at 1st position
'''

def find_first_position(n, array):
    start = 0
    end = len(array)

    while start < end:
        mid = (start+end)//2
        if array[mid] >= n:
            end = mid
        else:
            start = mid+1
    return start


n = 2
array = [1,2,3,4,5,6]
print(find_first_position(n, array))
