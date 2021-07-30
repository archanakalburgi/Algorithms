'''
m = number of rows 
n = number of columns 
row = []
column = []


'''

def maxArea(m, n, rowRemoved, columnRemoved):
    col = list(range(n+1))
    ro = list(range(m+1)) 
    areas = []
    for i in rowRemoved:
        if i in ro:
            ro.remove(i) 

    for j in columnRemoved:
        if j in col:
            col.remove(j) 

    print(ro)
    print(col) 

    for r in range(len(ro)):
        for c in range(len(col)):
            areas.append((ro[r]-ro[r-1])*(col[c]-col[c-1]))  
    return areas

print(maxArea(5,8,[2],[2,3]))