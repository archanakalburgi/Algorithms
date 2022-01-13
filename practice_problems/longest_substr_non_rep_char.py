"""
3. Longest Substring Without Repeating Characters 

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

"""
s = "" => ""
    
s = "aab" => 2
    
s = "a" => 1

s = "ffbdenq" => 6

s = "ec vbrrr" => 6 

s = "12363" => 4


"ffbdenqee ijlmopytect"
 
 
 "ffbdenqee"
 
 fun(string)        # string = "ffbdenqee", string=fbdenqee
    visited={}      # {}
    count=0         # count=0
    
     iterate string: i      # i=0, 1 | i=0
        if string[i] not visited    # f 
            count += 1      # count=1, 6
            mark "f" not visited    # {f}
        else    #f
            return count,i # 1, 1, 6
            
     
 main(s)     # "ffbdenqee"
    index=0      # index=0  
    res_count=0     # res_count=0
    while index<len(s)      # 0<9 , 1<9
        count, new_index = fun(s[index:len(s)])     # fun("ffbdenqee"), count=1 new_index=1
            # fun("fbdenqee")
        index = new_index+index      # index=1
        res_count = max(res_count, count)   # res_c = 1
    return res_count
"""

class Solution:
    def helper(self, string):
        visited = set()
        count=0
        for i in range(len(string)):
            if string[i] not in visited:
                count+=1
                visited.add(string[i])
            else:
                return count
        return count
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        res_count=0
        while index<len(s):
            count = self.helper(s[index:len(s)]) 
            index = index+1
            res_count = max(res_count, count)
        return res_count