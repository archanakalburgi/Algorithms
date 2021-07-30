'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2


sort = [1,2,2,3,3,4], 7
[2,2,3]
[3,4] -> 2


array = [0,1,3,3.5,5], 9  
[1,3,4]
[5,3] 
[5,3] -> 2

5-8 = 3
3 in array 
2
5 < 8
9 > 8


Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which 
the time complexity is O(n log n). 
'''

class Solution:
    def minSubArrayLen(self, s, nums): # 3, [1,4,2] [1,2,4],3 
        start = 0 
        currentSum = 0
        minLength = 999

        for n in range(len(nums)): # n = 0, 1, 2 
            currentSum += nums[n] # csum = 1, 1+4=5, 0+2=2  
            
            while currentSum >= s : # 1<3, 5>3, 4>3, 0<3, 2<3 
                minLength = min(minLength, n-start+1) # len = min(999,1-0+1)=2, =min(999, 1-1+1)=2
                currentSum -= nums[start] # csum=5-1=4, csum=4-4=0 
                start += 1 # start=1, start=2
                
        if  minLength != 999:
            return minLength 
        return 0

sol = Solution() 
# print(sol.minSubArrayLen(5, [1,2,3])) 
print(sol.minSubArrayLen(7, [2,3,1,2,4,5]))