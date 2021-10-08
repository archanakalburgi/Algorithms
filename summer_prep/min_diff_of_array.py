'''
You are given two integer arrays a and b of the same length.
Let's define the difference between a and b as the sum of absolute differences of corresponding elements:
difference = la[e] b[e]l + la[1] b[1]l + la[a. length 1] b[b. length 111
You can replace one element of a with any other element of a . Your task is to return the minimum possible difference
between a and b that can be achieved by performing at most one such replacement on a . You can also choose to leave
the array intact.
Example
For a = [1, 3 5] and b = [5, 3, 1] , the output should be minDiffofArrays(a, b) = 4 .
    If we leave the array a intact, the difference is |1 5| + 13 3| + (5 1| = 8:
    If we replace a[0] with a[1] , we get a [3, 3, 5] and the difference is 13
    If we replace a[e] with a[2] , we get [5, 5] and the difference is 15
    If we replace a[1] with a[e] , we get a = [1, 1, 5] and the difference is |11 5| + |1 3| + |5 1| = 10
    If we replace a[1] with a[2] , we get [1, 5, 5] and the difference is |1 5| + |5 3| + |5 1| = 10
    If we replace a[2] with a[e], we get a [1, 3, 1] and the difference is 11
    If we replace a[2] with a[1] , we get a [1, 3, 3] and the difference is |1 5| + 13 3| + 1:
So the final answer is 4 since it's the minimum possible difference.
'''

def minDiff0fArrays (a, b):
    summation = 0
    for i in range (len(a)):
        summation += abs (a[i]-b[i])
    
        for j in range(len(a)):
            for k in range(len(a)):
                a[j] = a[k]
                curr_sum = 0
                for l in range (len (b)):
                    curr_sum += abs (a[l]-b[l])
            summation = min (summation, curr_sum)
    return summation