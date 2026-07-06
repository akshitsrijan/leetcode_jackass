class Solution:
    
    def findCircleNum(self, isConnected):
        
        n = len(isConnected)

        visited = set()

        def dfs(city):

            # visit all connected cities
            for neighbor in range(n):

                # connected and not visited
                if isConnected[city][neighbor] == 1 and neighbor not in visited:

                    visited.add(neighbor)

                    dfs(neighbor)

        provinces = 0

        # check every city
        for city in range(n):

            if city not in visited:

                # new province found
                provinces += 1

                visited.add(city)

                dfs(city)

        return provinces