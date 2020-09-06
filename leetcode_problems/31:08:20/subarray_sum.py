'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays 
whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

- double for loop 
- combinations
- dictionary 

'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for n in range(len(nums)) :
            for i in range(n):
                if sum(nums[:n]) == k :
                    count = count + 1
        return count 

# s = Solution()
# print(s.subarraySum([1,1,1], 2))  


def subarray(nums, start = 0, end = 0, subarray_array=[]):#[1,2,3]

    if nums:  # 1,2,3 s=0, e=0 len=3 | s=1, e=0 | s=0, e=1 | s=1, e=1 | s=2, e=1 | s=0, e=2 | s=1, e=2 | s=2, e=2 | 
        if end == len(nums):
            return subarray_array #[]
        elif start > end:    #s=1 > e=0        
            return subarray(nums, 0, end+1) #s=0, e=1 | s=0, e=2 | s=0, e=3
        else :
            subarray_array.append(nums[start : end+1]) #[[1]] | s=0, e=2 [[1],[1,2]] |[[1],[1,2],[2]], [[1],[1,2],[2],[1,2,3]],
            #[[1],[1,2],[2],[1,2,3],[2,3]] , [[1],[1,2],[2],[1,2,3],[2,3],[3]] 
            return subarray(nums, start+1, end) #s=1 e=0 | s=1, e=1 | s=2, e=1 | s=1, e=2| s=2, e=2 | s=3, e=2
    return subarray_array 

def subarray_sum(array, k):
    all_subarrays = subarray(array)
    # print(all_subarrays)

    result = map(sum, all_subarrays) 
    count = 0
    for i in result:
        if i == k:
            count = count+1
    # print(count)
    return k 

print(subarray_sum([1,1,1]))

# result [1,3,2,6,5,3]


# summ_array = []
# # summ = 0
# for sub in all_subarrays:
#     # summ = 0 
#     # print(sub) 
#     for j in sub :
#         # print(j)
#         summ = summ + j 
#         summ_array.append(summ) 
# print(summ_array)


# print(subarray_sum([1,2,3]))

''' 
[1,2,3,4]
 s     e
[1]
[1,2]
[1,2,3]
[1,2,3,4]

[1,2,3,4]
   s   e
[2]
[2,3]
[2,3,4]

[1,2,3,4]
     s e
[3]
[3,4]

[1,2,3, 4]
        se
[4]

can be generated using 2 for loops
but time complexity will be n^2


'''