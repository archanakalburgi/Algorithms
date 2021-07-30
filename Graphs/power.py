'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''

# class Solution(object): # does not return correct results for n<0
#     def myPow(self, x, n):
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
#         self.result = 1

#         def power(x,n):
#             if n == 0:
#                 return self.result
            
#             if n :
#                 self.result = x * self.result
#                 return power(x, n-1) 
#         power(x,n)
#         return self.result 

class Solution(object):
    def myPow(self, x, n):
        return x**n

sol = Solution()
print(sol.myPow(2,3)) 

'''
why was it's difficulty 'medium?'
what did i miss?
'''