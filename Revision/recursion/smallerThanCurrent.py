'''
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
'''

'''
steps 
1. understanding prob : 

2.  i/p : [5,3,2]
    o/p : [2,1,0]

3. psedo code 
array = []  
   
for i in range(0,len(input_array)):    # i = 0 , 1 , 2
    count = 0
    for j in range(0,len(input_array)): j = 0, 1 , 2  | j = 0, 1 , 2 | j = 0, 1, 2
        if num[i] < num[j]: # 5 !<5 ,5 < 3, 5 < 2 | 3 !< 5 , 3 !< 3, 3 < 2 | 2 !< 5, 2 !< 3 , 2 !< 2 
            count += 1 # count = 0, count = 1, count = 2 | count = 1 | count = 0
    array.aapend[count] # array = [2,1,0]
return array

complexity = O(n^2)

def smallerNumbersThanCurrent(self, nums):
'''

def smallerNumbersThanCurrent(num):
    array = []
    for i in range(0,len(num)):# i = 0 , 1 , 2    
        count = 0 
        for j in range(0,len(num)): # j = 0, 1 , 2  | j = 0, 1 , 2 | j = 0, 1, 2
            if num[i] > num[j]: # 5 !<5 ,5 < 3, 5 < 2 | 3 !< 5 , 3 !< 3, 3 < 2 | 2 !< 5, 2 !< 3 , 2 !< 2 
                count += 1 # count = 0, count = 1, count = 2 | count = 1 | count = 0
        array.append(count) # array = [2,1,0]
    return array

print(smallerNumbersThanCurrent([5,3,2])) 


'''
if num[0] < num[1]:
    count += 1 
    array.append(count)
smallerNumbersThanCurrent(num[1:],count)

base case : if we have numbers in the element 

'''

def smallerNumbersThanCurrent(num,count = 0, array=[], i=0, j=0): # [5,3,2], array = [] | [3,2]
    if nums :
        if num[i] > num[j]: # 5 > 3, 5 > 2 | 3 !< 2  
            count = count + 1  # count = 1 , 2 
        array.append(count) # array [2]
        return smallerNumbersThanCurrent(num[1:],count, array, i,j) # [3,2], [] |  


'''
   if num[0] > num[1]: 
IndexError: list index out of range

this happens at the last recursive call,
when num = [2]
just one element 

what you do :
i = 0, j = 0
pass as parameters 
''' 

print(smallerNumbersThanCurrent([5,3,2]))

#  **** cannot solve it using recursion since there is no base case  

