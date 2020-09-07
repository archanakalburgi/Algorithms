'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_string = ''
        length = 0
        for letter in s:
            if letter not in sub_string:
                sub_string += letter
                length = max(length, len(sub_string))
            else:
                break_string = sub_string.index(letter)
                sub_string = sub_string[break_string + 1:] + letter 
        return length



# # class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sub_string = ''
#         for letter in s:
#             if letter not in sub_string:
#                 sub_string += letter
#         return len(sub_string)

#         #         ans = max(ans, len(sub_string))
#         #     else:
#         #         cut = sub_string.index(letter)
#         #         sub_string = sub_string[cut+1:] + char 
#         # return ans

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))