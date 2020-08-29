'''class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = i+1 
        array = [] 
        for i in range(0, len(nums)-1):
            product = 1
            for j in range (len(nums)-1):
                product = (nums[i]-1) * (nums[j]-1)
            array.append(product)    
        return (max(array)) 

s2 = Solution()
print(s2.maxProduct([10,2,5,2])) '''

def maxProduct(self, nums):
    first_greatest = max(nums)
    nums.remove(first_greatest)
    second_greatest = max(nums)
    return (first_greatest-1) * (second_greatest-1)

print(maxProduct([1,5,4,5]))

