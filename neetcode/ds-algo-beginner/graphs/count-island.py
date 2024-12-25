import collections
from types import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r, c = len(grid), len(grid[0])
        count = 0
        visited = set()

        def  bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                x, y = q.popleft()
                for dr, dc in [[0, 1],[-1, 0], [1,0], [0, -1]]:
                    r, c = x+dr, y+dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1' and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r, c))

        for x in range(r):
            for y in range(c):
                if grid[x][y] == '1' and (x, y) not in visited:
                    count += 1
                    bfs(x, y)
        return count
