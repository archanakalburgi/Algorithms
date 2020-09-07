'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]

A = [1,2,2,3,4]
i = 0 , 1, binary(A[i:]) binarsy([2,2,3,4], 1 )
i = 1 , 2, binary(A[i:]) binarsy([2,3,4], 2) 2 is 2 is duplicated
Output: 2


Example 2:

Input: [3,1,3,4,2]
Output: 3
'''


'''
from sort import merge_sort 
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_array = merge_sort(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

time complecity :
n log n + n 
'''
'''
from collections import Counter
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        """
        count = Counter(nums)
        # print(count.items())
        for key, value in count.items(): 
            if value>1: 
                return key 
        print(result) 

# s = Solution()
# print(s.findDuplicate([1,3,4,4,2]))

''' 
            
''' time complexity = O(n) 

numbers in nums cannot be greater than len(nums)

so on number has to repeat exactly one time 
''' 

def merge(A, B):

    if len(A) == 0 and len(B) == 0:
        return [] 
    
    else :
        if len(B) == 0:
            return A 
        
        elif len(A) == 0:
            return B
        
        else :
            if A[0] < B[0] :
                return [A[0]]+ merge(A[1:], B)
            
            else :
                return [B[0]]+ merge(A,B[1:])

def merge_sort(array) :
    if len(array) == 1:
        return array 
    else : 
        mid = int((len(array)) / 2)  
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        sorted_array = merge(left_array, right_array) 
        return sorted_array 

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
    
def find_duplicate(nums):
    sorted_array = merge_sort(nums)
    for i in nums:
        res = binary_search(nums[i:],i)
        if res :
            return i 
         

print(find_duplicate([1,2,2,3,4,5])) 

'''
modifying merge_sort to return the element if same 
    couldn't obtain as the subproblem different - sorting and returning the duplicate element 
'''

