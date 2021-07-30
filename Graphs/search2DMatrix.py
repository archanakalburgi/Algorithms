'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from start to end.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:
Input: matrix = [], target = 0
Output: false
'''

'''
make one list 
perform binary search
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        row = len(matrix)
        column = len(matrix[0])

        start = 0
        end = row * column - 1 

        while start <= end: 
            mid = (start + end) // 2 

            midElement = matrix[mid // column][mid % column]

            if midElement == target:
                return True

            if midElement > target:
                end = mid - 1
            else:
                start = mid + 1 
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
sol = Solution()
print(sol.searchMatrix(matrix, 100))