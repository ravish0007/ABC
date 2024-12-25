class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLUMNS = len(matrix), len(matrix[0])


        bottom, top = ROWS - 1, 0
        while top <= bottom:
            row = (top+bottom)//2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        l, r = 0, COLUMNS - 1

        while l <= r:
            mid = (l+r)//2

            element = matrix[row][mid]

            if target > element:
                l = mid + 1
            elif target < element:
                r = mid - 1
            else:
                return True
        return False
