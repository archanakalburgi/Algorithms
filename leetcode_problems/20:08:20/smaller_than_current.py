'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 
Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).


i/p : [8,   1,  2,  2,  3] 
            s
max = 8 
o/p : [4,0,1,1,3]
'''

# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         output = []
#         for i in range(len(nums)) :
#             count = 0
#             for j in range (len(nums)): 
#                 if nums[i] > nums[j]:
#                     count = count + 1   
#             output.append(count)           
#         return output   
    
# sol = Solution()
# print(sol.smallerNumbersThanCurrent([6,5,4,8])) 

'''
time taken will be n^2
'''

def smallerNumbersThanCurrent(nums,op_list=[], count=0, i=0, j=0):
    # op_list = [] 
    # count = 0
    if nums:
        if nums[i] > nums[j]:
            count = count + 1
        op_list.append(count)
        return smallerNumbersThanCurrent(nums[1:],op_list,count,i,j) 

    else :
        return op_list 
        

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
 