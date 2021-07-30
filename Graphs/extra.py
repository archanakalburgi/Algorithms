class Solution(object):
    def canVisitAllRooms(self, rooms):

        def dfs(aRoom, rooms):
            visited[aRoom] = 1
            for keys in rooms[aRoom]:
                if not visited[keys]:
                    dfs(keys, rooms)   
        
        numOfRooms = len(rooms) 
        visited = [0]* numOfRooms # mark room not visited
        
        dfs(0,rooms)

        return 0 not in visited 


rooms = [[1],[2],[3],[]]
sol = Solution()
print(sol.canVisitAllRooms(rooms))