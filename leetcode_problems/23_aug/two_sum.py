'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object): 
    def twoSum_iretation(self, nums, target):
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target :
                    return [i,j]


'''complexity will be n^2 
because 
for every i in first for loop, n for loop will be executed 
n*n is the time complexity 

exponential growth '''


class Solution(object): 
    def twoSum_dict(self, nums, target):
        dictnry = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if target - nums[i] in dictnry:
                return [dictnry[remaining], i]
            else :
                dictnry[remaining] = i

# sol = Solution()
# print(sol.twoSum([3,2,3],6))     

'''
-> target = a + b 
we need to return index of a and index of b 

-> b = target - a 

-> store
target-a : index 
(difference taeget-a = b)in a dictionary 

- iterate through list 

- when you find b return the index of a and b 

(index of a = dictionary[target - nums[i]] (will give value, indec in this case) 
index of b = i)

time complexity will be n. 

is there a way to do it without using dictionary ?

'''

def two_sum_sorting(nums, target):
    def merge(A, B):
        if len(A) == 0 and len(B) == 0:
            return []   
        else :
            if len(B) == 0 :
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

    def binary_search(array,key):
        start = 0
        end = len(array)-1
        while start <= end:
            mid = (start + end)//2
            if key < array[mid]:
                end = mid - 1 
            elif key > array[mid] :
                start = mid + 1 
            else :
                return mid   
            
        return None 

    sorted_array = merge_sort(nums) 

    for i in sorted_array:
        remaining = target - i
        sorted_index = binary_search(sorted_array, remaining) 
        if sorted_index :
            return  nums.index(i) ,nums.index(sorted_array[sorted_index]) 

print(two_sum_sorting([11,2,7, 15], 9)) 

'''
time complexity :
sorting     : n log n 
bs          : n log n 
for         : n 

2 (n log n)
n log n + n
'''