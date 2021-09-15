def helper(nums, start, end, subarrayList):  
	if end == len(nums):
		return subarrayList
	if nums:  
		if start > end:          
			return helper(nums, 0, end+1,subarrayList)
		else :
			subarrayList.append(nums[start : end+1]) 
			return helper(nums, start+1, end, subarrayList) 
        
	return subarrayList 

print(helper([1,2,3,4],0,0,[]))