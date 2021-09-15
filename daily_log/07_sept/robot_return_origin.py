'''
657. Robot Return to Origin


There is a robot starting at position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. 
Valid moves are R (right), L (left), U (up), and D (down). 
If the robot returns to the origin after it finishes all of its moves, return true. 
Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. 
"R" will always make the robot move to the right once, "L" will always make it move left, etc. 
Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:

Input: "UD"
Output: true 
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, 
so it ended up at the origin where it started. Therefore, we return true.
 

Example 2:

Input: "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. 
We return false because it is not at the origin at the end of its moves.

'''


'''
1. we could solve using dictionay , 
- store all the characters (U D R L) as keys 
- specify what they do as values 
'''

'''
divide and conquer 
    sort
    binary search ? 
'''

'''
what is required ?
    robot needs to move on 2D plane (x,y)

moves up and down ->    moves along y axis 
moves right and left -> moves along x axis  

up -> positive y axis
down -> negetive y axis 

right -> positive x axis
left -> negetive x axis 

starting point = [0,0]

complimentry sets :
    UD
    RL
    these will result in 0, the origin position

- go through all letters in the string 
- cancel out the complementry letters 
- if nothing remains -> return True
- else return False 
'''

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for i in range(0, len(moves)):
            if moves[i] == 'U':
                y += 1
            if moves[i] == 'D':
                y -= 1 
            if moves[i] == 'R':
                x += 1
            if moves[i] == 'L':
                x -= 1

        if x == 0 and y == 0:
            return True

        else:
            return False 

sol = Solution()
print(sol.judgeCircle('URDL')) 