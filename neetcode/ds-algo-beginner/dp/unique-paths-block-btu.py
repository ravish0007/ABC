
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * cols
        prev_row[-1] = 1 if obstacleGrid[-1][-1] == 0 else 0
        print('prev', prev_row)
        for i in range(rows-1, -1, -1):
            curr_row = [0] * cols
            curr_row[-1] = 0 if (obstacleGrid[i][-1] == 1 or prev_row[-1] == 0) else 1
            for c in range(cols - 2, -1, -1):
                if obstacleGrid[i][c] == 1:
                    curr_row[c] = 0
                else:
                    curr_row[c] = curr_row[c+1] + prev_row[c]
            print(curr_row)
            prev_row = curr_row
        return prev_row[0] 

