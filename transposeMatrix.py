class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transposedMatrix = []

        for i in range(len(matrix[0])):
            transposedMatrix.append([])

        for row in matrix:
            for i in range(len(row)):
                transposedMatrix[i] += [row[i]]
        
        return transposedMatrix