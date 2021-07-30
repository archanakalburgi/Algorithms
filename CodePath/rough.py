class Solution:
    def helper(self,nums, start, end, subarrayList):  
        if end == len(nums):
                return subarrayList
        if nums:  
            if start > end:          
                return self.helper(nums, 0, end+1,subarrayList)
            else :
                subarrayList.append(nums[start : end+1]) 
                return self.helper(nums, start+1, end, subarrayList) 
        
        return subarrayList 
            
        
    def maxSubArray(self, nums: List[int]) -> int:
        subarrays = self.helper(nums,0,0,[])
        max_sum = float('-inf')
        for array in subarrays:
            max_sum = max(max_sum, sum(array))
        return max_sum 


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maximum = nums[0]
#         element = nums[0]
#         for i in range(1,len(nums)):
#             element = max(element + nums[i], nums[i])
#             maximum = max(maximum, element)
#         return maximum 
