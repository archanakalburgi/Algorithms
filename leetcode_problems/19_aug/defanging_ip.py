'''
1108
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1" 
''' 

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')

sol = Solution()
print(sol.defangIPaddr('256.256.180.50')) 

'''
linear growth 
'''
