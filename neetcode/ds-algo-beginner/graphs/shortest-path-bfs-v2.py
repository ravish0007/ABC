class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        q.append((0, 0, 1))
        visited.add((0, 0))
       
        while q:
            r, c, length = q.popleft()
            print(r,c)
            
            if min(r, c) < 0 or max(r, c) >= rows or grid[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return length

            for dr, dc in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                x, y = r+dr, c+dc
                if (x,y) not in visited:
                    q.append((x,y,length+1))
                    visited.add((x,y))
        
        return -1
