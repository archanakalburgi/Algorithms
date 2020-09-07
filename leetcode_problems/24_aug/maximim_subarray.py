import itertools 

def max_subarray(array):
    all_cominations = []
    sum_array = []
    for i in range(0,len(array)+1):
        comb_array = list(itertools.combinations(array,i)) 
        all_cominations.append(sum(comb_array))
        print(all_cominations) 
    
    for combn in all_cominations: 
        print(combn)
        # sum_array.append(sum(combn))
    
    max_sum = max(sum_array)
    return max_sum

print(max_subarray([4,1,3])) 
 

'''
[-2,1,-3,4,-1,2,1,-5,4]

[4,1,3]

[(), (1), (4), (3), (4,1), (4,3), (1,3), (4,1,3)] 
0,1,4,3,5,7,4,8



for comb in all_comb:

'''








'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


from -2

-2+1                = -1    max = 2
-2+1-3              = -4
-2+1-3+4            = 0
-2+1-3+4-1          = -1
-2+1-3+4-1+2        = 1 
-2+1-3+4-1+2+1      = 2
-2+1-3+4-1+2+1-5    = -3
-2+1-3+4-1+2+1-5+4  = 1

from 1

1-3                 = -2    max = 4
1-3+4               = 2
1-3+4-1             = 1
1-3+4-1+2           = 3
1-3+4-1+2+1         = 4
1-3+4-1+2+1-5       = -1 
1-3+4-1+2+1-5+4     = 3 

from -3 

-3+4                = 1     max = 3
-3+4-1              = 0
-3+4-1+2            = 2
-3+4-1+2+1          = 3
-3+4-1+2+1-5        = -2
-3+4-1+2+1-5+4      = 2

from 4 

4-1                 = 3     max = 6
4-1+2               = 5
4-1+2+1             = 6
4-1+2+1-5           = 1
4-1+2+1-5+4         = 5

from -1

-1+2                = 1     max = 2
-1+2+1              = 2 
-1+2+1-5            = -3
-1+2+1-5+4          = 1

from 2

2+1                 = 3     max = 3
2+1-5               = -2
2+1-5+4             = 2

from 1

1-5                 = -4    max = 0
1-5+4               = 0

from -5 
-5+4                = -1    max = -1


max_array = [2,4,3,6,3,3,0,-1]

max(max_array) = 6
'''

'''
class Solution(object):
    def maxSubArray(self, nums):
        max_array = []
        
        if len(nums) == 1 or len(nums) == 0: 
            return nums[0]

        if len(nums) == 2:
            if nums[0] < 0 or nums[1] < 0:
                return max(nums)
            else :
                return nums[0]+nums[1]
        
        else :
            for i in range(0,len(nums)-1):
                sum = 0
                sum = sum + nums[i]
                addition_array = []
                for j in range(i+1, len(nums)):
                    sum = sum + nums[j]
                    addition_array.append(sum) 
                max_array.append(max(addition_array))

            return max(max_array) 

# s = Solution()
# array = [-2,1,-3,4,-1,2,1,-5,4]
# print(s.maxSubArray([2,1]))
'''