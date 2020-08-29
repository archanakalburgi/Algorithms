'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1: 

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {} 
        majority = len(nums) // 2
        for i in nums :
            if i in count_dict : 
                count_dict[i] += 1
            else :
                count_dict[i] = 1

        # print(count_dict.keys())
        # print(count_dict.values()) 
        for count in count_dict:
            if count_dict[count] > majority :
                return count

nums = [3,3,2,3,1,3]
s = Solution()
print(s.majorityElement(nums)) 