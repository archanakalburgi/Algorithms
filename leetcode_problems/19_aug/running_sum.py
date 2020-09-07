'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''


class Solution(object):
    def runningSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            sum_array = []
            sum = 0 
            for i in range(0, (len(nums))):
                sum = sum + nums[i]
                sum_array.append(sum)
            return sum_array

sol = Solution()
print(sol.runningSum([1,1,1,1])) 

'''
complexity : 
time increases as the input size increases 

it's a linear growth 
'''