class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowsCreated = 0
        rows = []
        previousRow = []

        while rowsCreated <= rowIndex:
            if len(previousRow) == 0:
                row = [1]
                rows.append(row)
                previousRow = row
                rowsCreated += 1

            elif len(previousRow) == 1:
                row = [1,1]
                rows.append(row)
                previousRow = row
                rowsCreated += 1
            else:
                row = [1]
                for i in range(len(previousRow)-1):
                    row.append(previousRow[i] + previousRow[i+1])
                row.append(1)
                rows.append(row)
                previousRow = row
                rowsCreated += 1

        return rows[rowIndex]