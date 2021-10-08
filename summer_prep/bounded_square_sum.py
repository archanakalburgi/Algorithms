'''
You are given two arrays of integers a and b, and two integers lower and upper
Your task is to find the number of pairs (i, j) such that lower ≤ a[i] * a[i] + b[j]
* b[j] ≤ upper
Example
® For a = [3,-1 b = [100, 5,-21 , lower = 7 , and upper = 99 the
output should be boundedSquareSum(a, b, lower, upper)
There are only four pairs that satisfy the requirement:
o If : 0 and j = 1, then a[e] = 3 b[1] = 5 and 7 ≤ 3 * 3 + 5 *
5 : ) + 25 = 36 ≤ 99
O f and j then a[0] = 3 , b[2] = 2 and 7 ≤ 3 * 3 +
(-2) * (-2) = 9 + 4 = 13 ≤ 99
o If i = 1 and j = 1, then a[1] =-1 b[1] = 5 and 7 ≤ (-1) *
(-1) + 5 * 5 = 1 + 25 : 26 ≤ 99
O If i = 2 and j = 2, then a[2] = 9 b[2] = 2 and 7 ≤ 9 * 9 +
(-2) * (-2) = 81 + 4 = 85 ≤ 99
• For a = [1, 2, 3,-1,-2,-3] b = [10] lower = 0 and upper = 100
the output should be boundedSquareSum(a, b, lower, upper) = 0
Since the array b contains only one element 10 and the array a does not
contain it is not possible to satisfy ≤ a[i] * a[i] + 10 * 10 ≤ 100
'''

def boundedSquareSum(a, b, lower, upper):
    count = 0
    for i in range(len(a)):
        if a[i]*a[i] < upper:
            for j in range(len(b)):
                if lower <= a[i]*a[i] + b[j]*b[j] <= upper:
                    count = count+1 
    return count 