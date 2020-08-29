'''We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique 
(except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

[[1,3],[-2,2]]
1^2 + 3^2 = 1+9 = 10
-2^2 + 2^2 = 4+4 = 8
'''

from math import sqrt 
class Solution(object):
    def kClosest(self, points, k):

        dis_tuple = () 
        dis_tuple_list = [] 
        points_array = []
    
        for pt in points : 
            distance = sqrt(abs(((pt[0])**2)+((pt[1])**2)))
            dis_tuple = (pt,distance)  
            dis_tuple_list.append(dis_tuple) 
            points_array.append(distance)

        k_points = [] 
        for i in range(0,len(points_array)):
            smallest_dis = min(points_array) 
            for tup in dis_tuple_list :
                if smallest_dis in tup :
                    k_points.append(tup[0])  
            points_array.remove(smallest_dis)
        return k_points[:k]

# points = [[1,1],[-2,2],[1,3]] 
points = [[0,1],[1,0]] 
s = Solution()
print(s.kClosest(points,2))  