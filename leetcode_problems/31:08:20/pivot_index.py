'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index 
is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, 
you should return the left-most pivot index.

 
Example 1:

Input: nums = [1,7,3,6,5,6]
[1,7,3,6,5,6]
 0,1,8,       11  
total = 28
left_sum = 0
right_sum = 0  

Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
'''

'''
i/p -> [1,7,3,6,5,6]
is 1 = 3+6+5+6 no
is 1+7 = 6+5+6 no
is 1+7+3 = 5+6 yes:
    return index[6] -> 3 
'''


class Solution(object):
    def pivotIndex(self, nums):
            total_sum = sum(nums)
            for i in range(len(nums)):
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
            return -1

# no of steps : 13 


'''
class Solution(object):
    def pivotIndex(self, nums):
        for i in range (len(nums)):
            if sum(nums) - sum(nums[:i]) == sum(nums[:i+1]): 
                return i 

        return -1 
        # no of steps : 13  
'''

''' 
def pivotIndex(nums):
    if nums == []:
        return -1
    else:
        if sum(nums) - sum(nums[:1]) == sum(nums[:1]): 
            return sum(num[])
'''

# s = Solution()
# print(s.pivotIndex([1,7,3,6,5,6]))
 
# print(pivotIndex([1,7,3,6,5,6])) 

'''for right index:
total_sum - left_sum - num[i] = left_sum 
- the current number isn't the part of the left or the right sum 
- '''

def pivot_index1(nums):
    total_sum = 0 
    for i in range(len(nums)):
        total_sum = total_sum + nums[i] 
    left_sum = 0 
    for i in range(len(nums)):
        if i != 0 :
            left_sum = left_sum + nums[i-1]
        if total_sum - left_sum - nums[i] == left_sum:
            return i 

    return -1

# print(pivot_index1([1,7,3,6,5,6])) 


def binary_search(array, key):
    mid = int(len(array)/2) 
    if len(array) >=1:
        if key == array[mid] :  
            return True
        
        if key < array[mid] :
            return binary_search(array[0 : mid], key) 

        if key > array[mid] :
            return binary_search(array[mid+1 : len(array)], key) 

    return False 

def pivot_index2(nums):
    left_sum = 0
    left_sum_array = []
    right_sum = 0
    right_sum_array = [] 
    reversed_nums = nums[::-1]
    # print(reversed_nums)
    for i in range(len(nums)):
        left_sum = left_sum + nums[i]
        left_sum_array.append(left_sum) 
    # print(left_sum_array)
    # [1, 8, 11, 17, 22, 28]

    for j in range(len(reversed_nums)):
        right_sum = right_sum + reversed_nums[j]
        right_sum_array.append(right_sum) 
    # print(right_sum_array)
    # [6, 11, 17, 20, 27, 28]

    '''
    we can use binary search to fing the same sum bur instead we can use one more for loop to search
    but that will be n^2 so use binary search
    '''
    for k in range(len(left_sum_array)):
        res = binary_search(right_sum_array[k:],left_sum_array[k])
        
       
print(pivot_index2([1,7,3,6,5,6]))