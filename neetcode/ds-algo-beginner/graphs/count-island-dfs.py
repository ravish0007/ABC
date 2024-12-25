class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r, c = len(grid), len(grid[0])
        count = 0


        def  dfs(i, j):

            if i < 0 or j < 0 or i == r or j == c or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x, y)

        return count
