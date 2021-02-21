class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
            
        first = -999
        
        totalDist = 0
        
        for nut in nuts:
            distToSqrl = abs(squirrel[0]-nut[0]) + abs(squirrel[1]-nut[1])
            distToTree = abs(tree[0]-nut[0]) + abs(tree[1]-nut[1])
                        
            if (distToTree-distToSqrl) > first:
                first = distToTree - distToSqrl        

            totalDist += 2 * distToTree
            
        
        totalDist = totalDist - first
        
        return totalDist

sol = Solution()

# Height : 5
# Width : 7
# Tree position : [2,2]
# Squirrel : [4,4]
# Nuts : [[3,0], [2,5]]

print(sol.minDistance(5,7,[2,2],[4,4],[[3,0],[2,5]])) 