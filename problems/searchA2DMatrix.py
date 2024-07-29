class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target:
                if target in row:
                    return True
            else:
                break
        
        return False