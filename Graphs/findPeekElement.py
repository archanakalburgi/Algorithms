'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.

'''

'''
binary search :
peek element : retrun the index of middle element 

cases   start   middle  end
1       0       1       2
2       1       0       2
3       2       1       0
4       0       2       1  -> peek case 

s < m < e
s < m > e
s > m < e
s > m > e 

keep moving the start to the right -> towards end 
return start 
'''
class Solution(object):
    def findPeakElement(self, nums): # [1,2,1]
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0 # start = 0
        end = len(nums)-1 # end = 3
        
        while start < end: # 0 < 3, 0 < 1 , 1 = 1 

            mid = (start+end) // 2 # mid = 1 , 0

            if nums[mid] > nums[mid+1]: # 2 > 1 , 1 < 2
                end = mid # end = 1 
            else:
                start = mid+1 # start = 1
        
        return start # 1 

nums = [1,2,1]
sol = Solution()
print(sol.findPeakElement(nums)) 