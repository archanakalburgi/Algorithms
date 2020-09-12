'''
435 
Given a collection of sorted_intervals, find the minimum number of sorted_intervals you need to remove to 
make the rest of the sorted_intervals non-overlapping.

 
Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of sorted_intervals are non-overlapping.



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



for example to have non overlapping sorted_intervals:
    - can remove A and B or
    - can remove D

prob asks for minimum removal so, remove D (only one interval removed)


how ??
(may be recursion)
- if only 1 interval : no overlap , so return 0 (no interval removed)

how to check if an interval is overlapping with another interval or not?
    - somehow sort sorted_intervals
    - compare sorted_intervals and see if they are overlapping 
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

from  typing import List 
class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        def comparatorInt(a: int  ,b: int ) -> bool:
            return a < b 

        def comparatorList(a: List[int] , b: List[int]) -> bool :
            return a[1] < b[1]

        def comparatorTuple(a : tuple , b : tuple ) -> bool :
            return a[1] < b[1]

        def merge(A,B, comp):
            i = 0
            j = 0
            C = [] 
    
            while i <= len(A)-1 and j <= len(B)-1 :
                if comp(A[i], B[j]):
                    C.append(A[i])
                    i+=1
        
                else:
                    C.append(B[j]) 
                    j+=1
    
            C.extend(A[i:])
            C.extend(B[j:])
    
            return C 


        def merge_sort(array, comp) :
            if len(array) == 1:
                return array 
            else : 
                mid = int((len(array)) / 2)  
                left_array = merge_sort(array[:mid],comp)
                right_array = merge_sort(array[mid:],comp)
                sorted_array = merge(left_array, right_array, comp) 
                return sorted_array

        if intervals == []:
            return 0
            
        sorted_intervals = merge_sort(intervals, comparatorList) 
        # print(sorted_intervals)   

        n = len(sorted_intervals)
        count = 0
        previous = 0

        if n < 2 :
            return 0

        # for i in range (1,n):
        #     if sorted_intervals[i][0] < sorted_intervals[previous][1]:
        #         count += 1 
        #         if sorted_intervals[i][1] < sorted_intervals[previous][1]:
        #             previous = i 
        #         else :
        #             previous = i
        # return count  

        for i in range (1,n):
            if sorted_intervals[i][0] < sorted_intervals[i-1][1]: # overlapping 
                count += 1       
                sorted_intervals[i][1] = min(sorted_intervals[i][1],sorted_intervals[i-1][1])
                # storing min so that the intervals become continous to compare with the next element
        return count 
c
        

        # while(right < n):
        #     if sorted_intervals[left][1] <= sorted_intervals[right][0]:
        #         left = right 
        #         right += 1 

        #     if sorted_intervals[left][1] <= sorted_intervals[right][1]:
        #         count += 1
        #         right += 1 

        #     if sorted_intervals[left][1] > sorted_intervals[right][1]:
        #         count += 1
        #         left = right 
        #         right += 1 

        # return count 
         

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) 
print(sol.eraseOverlapIntervals([[1,2]])) 
print(sol.eraseOverlapIntervals([])) 