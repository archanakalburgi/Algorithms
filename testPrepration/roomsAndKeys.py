class Solution(object):
    def canVisitAllRooms(self, rooms):
        noOfRooms = len(rooms)
        visited = [0]*noOfRooms

        def visitRoom(aRoom, rooms):
            visited[aRoom] = 1
            for keys in rooms[aRoom]:
                if visited[keys] == 0:
                    visitRoom(keys, rooms)
        
        visitRoom(0, rooms)
        return 0 not in visited

rooms = [[1,3],[3,0,1],[2],[0]] 
sol = Solution()
print(sol.canVisitAllRooms(rooms))