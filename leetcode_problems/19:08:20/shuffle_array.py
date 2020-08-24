'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].'''

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        if len(nums) % n == 0:
            array = []
            array1 = nums[:n]
            array2 = nums[n:]
            for i in range(0,len(array1)):
                array.append(array1[i])
                array.append(array2[i])
        return array 

sol = Solution()
nums = [2,5,1,3,4,7]
print(sol.shuffle(nums,3))

'''
linear growth 
time increases with increase in the size of input 
'''
