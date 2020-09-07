'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''


# class Solution(object):
#     def subtractProductAndSum(self, n):
#         array = map(int,str(n))
#         # map(function, iterable),
#         # Apply function to every item of iterable and return a list of the results.
#         product = 1
#         addition = 0
#         for i in array :
#             product = product * i 
#             addition = addition + i  

#         return (product - addition)

# sol = Solution()
# print(sol.subtractProductAndSum(4421))  

'''
time taken is n 

linear growth 
'''

class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        summ = 0 
        while n:
            digit = n % 10
            product = product * digit 
            summ = summ + digit 
            n = n // 10 

        return (product - summ)
    
sol = Solution()
print(sol.subtractProductAndSum(23)) 