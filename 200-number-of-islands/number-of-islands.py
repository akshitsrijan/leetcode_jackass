'''class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        rows =len(grid)
        cols=len(grid[0])

        islands=0

        def dfs(r,c):

            #boundary checks
            if r<0 or c<0 or r>=rows or c>=cols:
                return 

            #water or visited
            if grid[r][c] !=1:
                return 1

            
            #mark visited
            grid[r][c]='0'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            #traverse whole grid
            for r in range(rows):
                for c in range(cols):

                    #found new island
                    if grid[r][c] == '1':
                        islands = islands +1

                        #sink entire island
                        dfs(r,c)
            return islands
            
            '''
class Solution:
    
    def numIslands(self, grid):
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(r, c):

            # boundary checks
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # water or visited
            if grid[r][c] != '1':
                return

            # mark visited
            grid[r][c] = '0'

            # explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # traverse whole grid
        for r in range(rows):
            for c in range(cols):

                # found new island
                if grid[r][c] == '1':

                    islands += 1

                    # sink entire island
                    dfs(r, c)

        return islands
        