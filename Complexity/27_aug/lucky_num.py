import collections
class Solution:
    def findLucky(self, arr) :
        count = collections.Counter(arr)
        max_count = -1
        for key in count :
            if key == count[key]:
                max_count = max(max_count, key)
        return max_count


            


s = Solution()
print(s.findLucky([4,2,3])) 

'''
using dictionary : takes longer 


sorting 
[2,3,4] ??

counter method 

>>> array = [1,2,2,3,3,3]
>>> Counter(array)
Counter({3: 3, 2: 2, 1: 1})
>>> c = Counter(array)
>>> c.keys()
[1, 2, 3]
>>> c.values()
[1, 2, 3]
>>> c[3]
3
'''