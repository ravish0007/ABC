class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))

        length = 1

        if grid[0][0] == 1:
            return -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if (r == rows - 1) and (c == cols - 1):
                    return length
                for dr, dc in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    x,y = r+dr, c+dc
                    if x < 0 or x == rows or y < 0 or y == cols or (x,y) in visited or grid[x][y] == 1:
                        continue
                    q.append((x,y))
                    visited.add((x,y))
            length += 1

        return -1
