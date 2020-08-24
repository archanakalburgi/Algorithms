'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 
Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
'''

'''
list.insert(i, x) : Insert an item at a given position. 
The first argument is the index of the element before which to insert, 
so a.insert(0, x) inserts at the front of the list,
and a.insert(len(a), x) is equivalent to a.append(x). 
'''



class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
        # target_array = [] 
        # for i in range(len(nums)):
        #     target_array.append(nums[index[i]]) 
        # return target_array


    
sol = Solution()
print(sol.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))  


'''linear growth '''