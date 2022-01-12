"""
You are given an array of non-negative integers numbers . 

You are allowed to choose any number from this array and swap any two digits in it. 
If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be
considered just 10 ).

Your task is to check whether it is possible to apply the swap operation at most once, SO
that the elements of the resulting array are strictly increasing.

Example
1. For numbers = [1, 5, 10, 20] , the output should be solution (numbers) = true
The initial array is already strictly increasing, so no actions are required.

2. For numbers = [1, 3, 900, 10] the output should be solution (numbers) = true
    - By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 s considered to
    be just 9 
    - So the updated array will look like [1, 3, 9, 10] , which is strictly increasing.

3. For numbers = [13, 31, 30] , the output should be solution (numbers) = false
    • The initial array elements are not increasing.
    • By swapping the digits of numbers[0] = 13 the array becomes [31, 31, 30] which is not strictly increasing;
    • By swapping the digits of numbers[1] = 31 the array becomes [13, 13, 30] which is not strictly increasing;
    • By swapping the digits of numbers[2] = 30 the array becomes [13, 31, 3] which is not strictly increasing;
    So, it's not possible to obtain a strictly increasing array, and the answer is false

4. For numbers = [12, 31, 30]
"""

import itertools
# permutation
def swap_check (num1, num2):
    s = str(num1)
    for i in itertools.permutations(s):
        swapped_num = int("". join(list(i)))
        if swapped_num < num2:
            return swapped_num
    return num1 

def is_strictly_increasing(numbers):
    for i in range (len (numbers)-1) :
        if numbers[i] >= numbers [i+1]:
            num = swap_check(numbers[i], numbers [i+1])
            numbers[i] = num
    return numbers

def solution (numbers):
    array = is_strictly_increasing(numbers)
    for i in range (len(array)-1):
        if array [i] >= array [i+1]:
            return False
    return True


numbers1 = [1, 3, 900, 10] # true
numbers2 = [13, 31, 30] # false
numbers3 = [527, 516, 216, 965, 951] # false
numbers4 = [92, 121, 193, 293, 328, 345, 343, 475, 478, 154, 258, 706, 9291] # false
numbers5 = [64, 281, 219, 259, 291, 299, 588, 352, 374, 421, 405, 497, 875, 648, 725, 832, 877, 911, 925, 929, 9543] # false
print(solution(numbers1))
print(solution(numbers2))
print(solution(numbers3))
print(solution(numbers4))
print(solution(numbers5))
