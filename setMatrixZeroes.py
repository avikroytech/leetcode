class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        columns = []

        for row in matrix:
            if 0 in row:
                for i in range(len(row)):
                    if row[i] == 0:
                        columns.append(i)
                matrix[matrix.index(row)] = [0]*len(row)
        
        for col in columns:
            for row in matrix:
                row[col] = 0
        
        return matrix