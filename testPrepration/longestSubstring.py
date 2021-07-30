'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
1. take out all the possible substrings 
2. get len of substrings with unique character 

problem : space and time : n^2

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]]+1)
                dic[s[i]] = i
            res = max(res, i-j+1)
        return res

s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))