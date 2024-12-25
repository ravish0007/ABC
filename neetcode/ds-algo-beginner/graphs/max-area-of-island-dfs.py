class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        visited = set()
        count = 0

        def dfs(i, j):
            if i < 0 or i == rows or j < 0 or j == cols or \
                grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i, j))

            return (1+ dfs(i+1,j) + dfs(i-1, j) + dfs(i, j+1) +dfs(i, j-1))

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x,y) not in visited:
                    count = max(count, dfs(x,y))
        
        return count

