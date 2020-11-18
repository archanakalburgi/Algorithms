def calculateMaxTime(n, curr, headID, manager, informTime):
    if curr not in employees:
        return 0
    
    children = employees[curr]
    maxTime = 0

    for child in children:
        maxTime = max(maxTime, calculateMaxTime(n, child,headID, manager, informTime)) 

    return informTime[curr] + maxTime 

employees = {
    -1 : [0],
    0  : [1, 2],
    1  : [3, 4],
    2  : [5, 6],
    3  : [7, 8],
    4  : [9, 10],
    5  : [11, 12],
    6  : [13, 14] 
}
n = 15
headID = 0 
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], 
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
curr = -1
print(calculateMaxTime(n, curr, headID, manager, informTime)) 