class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()

        fresh = 0
        time = 0

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and  q:
            for i in range(len(q)):
                r, c = q.popleft()
                print((r,c))
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1  
