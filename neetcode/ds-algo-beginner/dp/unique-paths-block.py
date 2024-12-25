class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * cols for i in range(rows)]
        

        def bruteforce(r, c):

            if r == rows or c == cols or obstacleGrid[r][c]:
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]
            
            if r == rows-1 and c == cols-1:
                return 1

            cache[r][c] =  bruteforce(r+1, c) + bruteforce(r, c+1)

            return cache[r][c]

        return bruteforce(0, 0)
