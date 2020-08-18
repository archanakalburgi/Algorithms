'''
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] 
in the shuffled string.
Return the shuffled string.

 
Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

'''

class Solution(object):
    def restoreString(self, s, indices):
        array = ['']*len(s) 
        new_string = '' 
        if len(s) == len(indices):
            for i in range(len(s)): 
                array[indices[i]] = s[i]  
            for i in array:
                new_string += i  
        return new_string   

sol = Solution()
print(sol.restoreString("codeleet", [4,5,6,7,0,2,1,3]))


'''
time taken = 2n 
linear growth 
'''
