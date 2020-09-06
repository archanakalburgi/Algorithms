'''
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[1...k].
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, 
we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return the k-values corresponding to a sequence of pancake flips that sort arr. 
Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

 

Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
Notice that we return an array of the chosen k values of the pancake flips.



Example 2:

Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).

'''


'''
flip : 
    fliping array from ith position : every element from ith position will be in reverse order 
    flip put 1st element at the last 

input - array
output - sorted array

to get sorted array - largest element must be at the bottom 
1 <= arr[i] <= arr.length -> given constraint (meaning no element can ne greater than the length of the array)


- put largest at first 
- flip the array 
-keep repeating the 2 steps till array is sorted -> largest elelemt at the end, smallest element at the begining


1. get largest element's index 
2. flip from the largest index(lafgest element)


example :
 0 1 2 3                retult = [3,4,2,3,2]
[3,2,4,1]

largest = 4 at 2
flip from 2 (3 elements flipped)
 0 1 2 3
[4,2,3,1]

largest = 4 at 0
when at 0 flip from n (4 elements flipped)

 0 1 2 3 
[1,3,2,4]

largest = 4 at 3, at n 
so look for next largest element 

next largest element = 3 

3 is at 1 

so flip from 1 (2 elements flipped)

 0 1 2 3
[3,1,2,4]

to place 3 at it's right position flip from 2

[2,1,3,4] (3 elements flipped)

next largest element = 2

flip from 1 (2 3l3m3nts flipped)
[1,2,3,4]

return result [3,4,2,3,2]

'''

class Solution(object):
    def pancakeSort(self, arr):
        result = []
        def flip (index):
            for i in range(0, index//2 + 1):
                temp = arr[i]
                arr[i] = arr[index-i]
                arr[index-i] = temp 
        
        for i in range(len(arr)-1, 0, -1):
            for j in range (1, i+1):
                if arr[j] == i+1:
                    flip(j)
                    result.append(j+1)
                    break 
            flip(i)
            result.append(i+1)
        return result 

sol = Solution()
print(sol.pancakeSort([3,2,4,1]))


'''
time complexity : n^2
'''

def pancakeSort(arr):
    def flip (index):
        for i in range(0, index//2 + 1):
            temp = arr[i]
            arr[i] = arr[index-i]
            arr[index-i] = temp 
        
    result = []
    n = len(arr)
    largest = n
    for i in range(n):
        largest_index = arr.index(largest)
        flip(largest_index)
        result.append(largest_index+1)
        flip(largest-1)
        result.append(largest)
        largest -= 1
    return result

print(pancakeSort([3,2,4,1]))      

'''
time complexity = n 

'''