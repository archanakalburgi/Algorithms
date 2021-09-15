from math import sqrt 
from m_s import merge_sort 
class Solution(object):
    def kClosest(self, points, k):

        dis_tuple = () 
        dis_tuple_list = [] 
        distance_array = []
    
        for pt in points : 
            distance = sqrt(abs(((pt[0])**2)+((pt[1])**2)))
            dis_tuple = (pt,distance) 
            dis_tuple_list.append(dis_tuple) 
            distance_array.append(distance)
        
        sorted_distance = merge_sort(distance_array)
          
        points = []
        for i in range(0,k):
            smallest_dis = sorted_distance[i] 
            for tup in dis_tuple_list :
                if smallest_dis in tup:
                    points.append(tup[0])  
        return points 

        '''
        k_points = [] 
        for i in range(0,len(distance_array)):
            smallest_dis = min(distance_array) 
            for tup in dis_tuple_list :
                if smallest_dis in tup :
                    k_points.append(tup[0])  
            distance_array.remove(smallest_dis)
        return k_points[:k] 
        '''

# points = [[1,1],[-2,2],[1,3]] 
points = [[0,1],[2,0],[3,0],[4,0]]  
s = Solution()
print(s.kClosest(points,3))