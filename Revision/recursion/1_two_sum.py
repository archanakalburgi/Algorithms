'''
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

'''
inputArray = [3,4,2] , target = 5
output = [0,2]

[3,4,2] 5 
5-3 = 2
if binary_search(2):
    return nums.index(3,2)


if target :
    target = target - nums[1]
    twoSum(nums[1:], target)
'''

def merge(a,b):
    if len(a) == 0 and len(b) == 0:
        return []
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a 
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:],b)
    if b[0] < a[0]:
        return [b[0]] + merge(a, b[1:])

def merge_sort(array):
    if len(array) == 1:
        return array 
    
    else :
        mid = len(array)//2

        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:]) 

        return merge(left,right)


def binary_search(sortedArray, key):
    mid = len(sortedArray) // 2
    
    if len(sortedArray) >= 1:

        if key == sortedArray[mid] :
            return True

        if key < sortedArray[mid] :
            return binary_search(sortedArray[0 : mid], key)  
    
        if key > sortedArray[mid] :
            return binary_search(sortedArray[mid+1 : len(sortedArray)],key) 
      
    return False 


def twoSum(array, target):
    # sorted_array = merge_sort(array) # sorted_array = [3,5,8], target = 13| [5,8], 13
    if array :
        sorted_array = merge_sort(array)
        diff = target - sorted_array[0] # diff = 13 - 3 = 10| diff = 13-5=8 
        res = binary_search(sorted_array, diff) # res = false | true
        if res :
            return [array.index(sorted_array[0]),array.index(diff)] 
        else : 
            return twoSum(sorted_array[1:],target) # [5,8]
        
print(twoSum(merge_sort([8,3,5]),13))   


'''
must pass sorted array, so cannot retrieve index by using recursion 
''
