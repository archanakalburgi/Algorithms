'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_list = []
        while x :
            temp = x % 10
            num_list.append(temp)
            x = x // 10
        for i in num_list:
            s = map(str, num_list)   
            s = ''.join(s)          
            s = int(s)              
        return s

s = Solution()
print(s.reverse(1234)) 