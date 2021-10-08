'''
Given an integer n and an array | a of length n your task is to apply the following mutation to a :
Array a mutates into a new array b of length n.

© For each i from e to b[i] = a[i 11 + a[i] + a[i + 1] .
If some element in the sum a[i 1] + a[i] + a[i + 1] does not exist, it should be
set to 0 For example, b[e] should be equal to 0 + a [0] + a[1]

Example
For n = 5 and a = [4, 0, 1,-2, 3] , the output should be mutateTheArray (n, a) = [4, 5,-1, 2 1] .
    b[0] = 0 + a[0] + a_1] = 0 + 4 + 0 = 4
    b[1] = a[0] + a[1] a[2] = 4 + 0 + 1 = 5
    b[2] = a[1] + a [2] a[3] = 0 + 1 + (-2) =-1
    b[3] = a[2] + a[3] + a[4] = 1 (-2) + 3 = 2
    b[4] = a[3] + a [4] + 0 = (-2) + 3 + 0 = 1

So, the resulting array after the mutation will be [4, 5,-1, 2, 1] .
'''

def mutateTheArray (n, a):
    b = list()
    if n > 1:
        for i in range(1, len(a)):
            b.append(sum(a[i-1: i+2]))
        return [a[0]+a[1]]+b
    return a 
