class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        visited = set()
        count = 0

        def bfs(i, j):
            count = 1
            visited.add((i, j))

            q = collections.deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    r, c = x+dr, y+dc
                    if (r in range(rows)) and (c in range(cols)) and (r, c) not in visited and grid[r][c] == 1:
                        count += 1
                        visited.add((r,c))
                        q.append((r,c))
            return count

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x,y) not in visited:
                    count = max(count, bfs(x,y))
        
        return count

