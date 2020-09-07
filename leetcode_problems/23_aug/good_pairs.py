'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.


Example 1:
              [0,1,2,3,4,5]
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.'''


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        array = []
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j :
                    array.append([i,j])
        return(len(array))

sol = Solution()
print (sol.numIdenticalPairs([1,2,3])) 

'''
complexity : n * n 
'''