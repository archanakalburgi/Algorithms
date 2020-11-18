'''
1376. Time Needed to Inform All Employees

A company has n manager_subordinates with a unique ID for each employee from 0 to n - 1. 
The head of the company has is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] 
is the direct manager of the i-th employee, manager[headID] = -1. 
Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the manager_subordinates of the company of an urgent piece of news. 
He will inform his direct subordinates and they will inform their subordinates and so on 
until all manager_subordinates know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates 
(i.e After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the manager_subordinates about the urgent news.


Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.


Example 2:
                            2
                        / / | \ \
                       / /  |  \ \
                      0  1  3  4  5

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the 
manager_subordinates in the company and needs 1 minute to inform them all.
The tree structure of the manager_subordinates in the company is shown.


Example 3:

    6
     \
      5
       \
        4
         \
          3 
           \ 
            2
             \
              1 
               \
                0

Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.


Example 4:

Input: n = 15, headID = 0, 
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], 
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform manager_subordinates 1 and 2.
The second minute they will inform manager_subordinates 3, 4, 5 and 6.
The third minute they will inform the rest of manager_subordinates.

manager_subordinates : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
managers  : [-1,0, 0, 1, 1, 2, 2, 3, 3, 4,  4,  5,  5,  6,  6]
adjList : {manager : manager_subordinates}
[
    -1 : [0],
    0  : [1, 2],
    1  : [3, 4],
    2  : [5, 6],
    3  : [7, 8],
    4  : [9, 10],
    5  : [11, 12],
    6  : [13, 14]
]

Example 5:

Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076
 

Constraints:

1 <= n <= 10^5
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the manager_subordinates can be informed.
'''


'''
Input: n = 15, headID = 0, 
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], 
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform manager_subordinates 1 and 2.
The second minute they will inform manager_subordinates 3, 4, 5 and 6.
The third minute they will inform the rest of manager_subordinates.

adjList : {manager : manager_subordinates}
[
    -1 : [0],
    0  : [1, 2],
    1  : [3, 4],
    2  : [5, 6],
    3  : [7, 8],
    4  : [9, 10],
    5  : [11, 12],
    6  : [13, 14]
]

    :type n: int
    :type headID: int
    :type manager: List[int]
    :type informTime: List[int]
    :rtype: int

    build graph from data :
       map managers(manager_subordinates) to subordinates

    - build dictionary : 'graph'
    graph[manager] : employee 

    - loop through manager array and assign manager_subordinates (how?)  

    dfs to find time to inform employee 
    - information should reach last person -> leaf node 
    - look for longest path 
    - add time needed 
    - return sum of time from one path
    - return max of all sum 
    (max sum path ???)
'''

import collections
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        # def dictinary(managers, manger):
        # index = []
        # for emp ,empManager in enumerate(managers):
        #     if empManager == manger:
        #         index.append(emp) 
        # return index

        # for m in managers:
        #     subordinates[m] = dictinary(managers, m)


        manager_subordinates = collections.defaultdict(list) 
        for idx, emp in enumerate(manager):
            manager_subordinates[emp].append(idx) 

        def calculateMaxTime(current):
            if current not in manager_subordinates:
                return 0
            
            children = manager_subordinates[current]
            maxTime = 0

            for child in children:
                maxTime = max(maxTime, calculateMaxTime(child)) 

            return informTime[current] + maxTime 
    
        return calculateMaxTime(headID)
    
n = 15
headID = 0 
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

sol = Solution()
print(sol.numOfMinutes(n, headID, manager, informTime))