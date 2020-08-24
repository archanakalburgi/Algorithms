'''Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello" '''

class Solution(object):
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        if string.islower():
            return string
        else:
            return string.lower()

sol = Solution()
print(sol.toLowerCase('SONG')) 