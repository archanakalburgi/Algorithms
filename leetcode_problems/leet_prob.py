class Solution(object):
    def runningSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            sum = 0 
            sum_array = []
            for i in range(0, (len(nums))):
                sum = sum + nums[i]
                sum_array.append(sum)
            return sum_array

sol = Solution()
print(sol.runningSum([1,2,3,4]))

def runningsum(array):
    if array :
        sum = 0
        return 

'''Q] Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Input: nums = [3,4,5,2]
Output: 12 

Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. '''

'''class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = i+1 
        array = [] 
        for i in range(0, len(nums)):
            product = 1
            product = (nums[i]-1) * (nums[j]-1)
            array.append(product)    
        return (max(array)) 

s2 = Solution()
print(s2.maxProduct([3,4,5,2])) '''


'''Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.'''

'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            if val in nums :
                nums.remove(val)
        return len(nums)  

S1 = Solution()
print(S1.removeElement([3,2,2,3], 3))''' 



'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

''' 
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mylist = list(dict.fromkeys(nums))
        

s = Solution()
s.findDuplicates([4,3,2,7,8,2,3,1])            '''


'''Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).'''
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = [] 
        for i in range (0, len(nums)):
            true_val = nums[i] 
            nums[i]=1
            product = 1
            for j in range(0, len(nums)):
                product = product * nums[j]
            array.append(product)
            nums[i] = true_val
        return array 

s1 = Solution()
print(s1.productExceptSelf([4,2,3])) 

# time exceeded - 17/18 tests passed 
'''


