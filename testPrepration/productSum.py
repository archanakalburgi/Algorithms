'''
A “special array” is a non-empty array that contains either integers or other “special arrays” 
(i.e. subarrays of integers). 
The product sum of a “special array” is the sum of its elements, 
where the inner “special arrays” are added themselves and 
then multiplied by how deep they are in the original array. 

For instance, 
the depth of [] is 1; 
the depth of the inner array in [[]] is 2; 
and the depth of the innermost array in [[[]]] is 3.


Taking in a “special array”, write a function that returns the product sum of a “special array”.
Sample Input: array=array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample Output: 12 (calculated as: 5 + 2 + 2*(7 + -1) + 3 + 2*(6 + 3 * (-13 + 8) + 4)

example : 
input : [1,2] 
output : 3
1*1 + 1*2

input : [1,2,[3,1],5,[[4]]]
Output : 21 
Explanation : 1*1 + 1*2 + 2*(3+1) + 1*5 + 3*4 = 3+6+12 = 21
'''

'''
special array : has integers or special array 
* indication that it is a recursion problem 

pass multiplier as a parameter to the recursive function and add 1 to it

[1,2,[3,1],5,[[4]]]
1+2+ 2*(3+1)+ 3*4 = 3+6+12 = 21

[ 1*1+ 1*2+ 2*(sum of elements) + 1*5 + depthati4*(sum of elements)...] => totalsum

            2*(sum of elements)
                                        3*(sum of elements)


    [  5, 2, * 3, *, 4]

    /               \
[7, -1]         [6, *]
                        \
                        [-13, 8]
                        
'''
# funcCall(array):
#     return func(array,1)

# func(array, depth): # [1,[[2]]] 
#     sum =0 # sum = 0
#     depth = 0 
#     for element 0 to len(array): # element = 1, [[2]]
#         if type(elemt) == int: # true
#             sum+=element*depth
#         if type(elemt) == List: # 
#             sum+= func(element,depth+1)
#     return sum

def productSum(array, depth=1):
    sum = 0
    for element in array:
        if type(element) == list:
            return productSum(element, depth+1)
        else:
            sum = sum+element
    return sum*depth

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])) 