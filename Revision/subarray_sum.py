'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays 
whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2 
'''


'''
eg : [1,1,1] ,2 
1+1 = 2
1+1 = 2

2

1. two for loops : 
    for i from 0 to len(nums):
        for j from 0 to i :
            if sum(nums[:n] == k):
                count += 1
    return count 

time complexity = O(n^2)

2. using recursion : 
    generate subarrays 
    find sum of each subarray
    return how many subarrays have sum = k 

generate_subarrays:
    if nums :

'''

# function to generate subarrays 
def subarray(nums, start = 0, end = 0, subarrayList=[]): # [1,1,1], 0, 0 

    if end == len(nums):
            return subarrayList

    if nums:  

        if start > end:          
            return subarray(nums, 0, end+1)

        else :
            subarrayList.append(nums[start : end+1]) #[1], [1,1], [1], [1,1,1], [1,1], [1]
            return subarray(nums, start+1, end) 

    return subarrayList  

def subarray_sum(array, k): 
    subarrays = subarray(array) 
    print(subarrays) 

    result = map(sum, subarrays) 
    count = 0
    for i in result:
        if i == k:
            count = count+1
    return k 

print(subarray_sum([1,1,1], 2)) 