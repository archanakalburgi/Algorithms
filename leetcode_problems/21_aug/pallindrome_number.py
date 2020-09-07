'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        reversed_string = "".join(list(reversed(string)))
        if reversed_string != string:
            return False
        return True

s = Solution()
print(s.isPalindrome(121))




