'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the 
largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        element = nums[0]
        for i in range(1,len(nums)):
            element = max(element + nums[i], nums[i])
            maximum = max(maximum, element)
        return maximum 

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))