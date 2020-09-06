'''
435 
Given a collection of intervals, find the minimum number of intervals you need to remove to 
make the rest of the intervals non-overlapping.

 
Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.



A = [1,2]   
B = [2,3]
C = [3,4]
D = [1,3]

start : A, D, B, C
end : A, B, D, C 



|-----------|-----------|-----------| 
1           2           3           4
1----A------2
            2-----B-----3
                        3-----C-----4
1-----------D-----------3



for example to have non overlapping intervals:
    - can remove A and B or
    - can remove D

prob asks for minimum removal so, remove D (only one interval removed)


how ??
(may be recursion)
- if only 1 interval : no overlap , so return 0 (no interval removed)

how to check if an interval is overlapping with another interval or not?
    - somehow sort intervals
    - compare intervals and see if they are overlapping 
    - if they overlap increase the counter 
    - return counter 


'''
'''
current and next 
current[end] >= next[begining] -> overlap 

3 case :
1. side by side 
2. partial cover 
3. totally covered
'''


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        def sort(array):
            for i in range(1,len(array)):
                j = i-1
                key = array[i] 

                while j >= 0 and array[j] > key:
                    array[j+1] = array[j]
                    j = j - 1
        
                array[j+1] = key 
            return array 

        sorted_intervals = sort(intervals)

        print(sorted_intervals) 
        
        # while len(intervals):

        #     if intervals[i][1] <= intervals[i+1][0]: # [1,2] [2,3] -> non overlapping 
                

        #     if intervals[i][1] <= intervals[i+1][1]: #[1,3] [2,4] -> overlapping 
                
            
        #     if intervals[i][1] > intervals[i+1][1]: # [1,6] [3,4]
            

        # return count 

sol = Solution()
print(sol.eraseOverlapIntervals([[3,8][1,3],[2,5]])) 