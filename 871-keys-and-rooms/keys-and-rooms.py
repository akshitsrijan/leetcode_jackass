class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()

        def dfs(room):
            visited.add(room)

            #explore keys
            for key in rooms[room]:

                if key not in visited:
                    dfs(key)
        #start from 0
        dfs(0)

        #check all rooms visited
        return len(visited) == len(rooms)