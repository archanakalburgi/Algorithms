"""
Given a rectangular matrix matrix and an integer frameSize, 
consider the outer frames of all frameSize × frameSize contiguous square submatrices of matrix. 

Your task is the following:

1. Calculate the sum of all numbers located on the frame of each frameSize × frameSize submatrix.
2. Determine the maximum of all these sums.
3. Find all the distinct numbers that appear in at least one of the frames of 
frameSize × frameSize submatrices with a sum equal to the maximum. 
Each integer from these square frames should be calculated exactly once. 
4. Return the sum of these distinct numbers.
Note: A frameSize × frameSize square frame contains max(1, 4 × (frameSize - 1)) cells. 
See example for better understanding
"""