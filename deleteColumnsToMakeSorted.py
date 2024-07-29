class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        cols = []

        for i in range(len(strs[0])):
            col = []
            for row in strs:
                col.append(row[i])
            cols.append(col)
        
        deleted = 0
        
        for col in cols:
            if col != sorted(col):
                deleted += 1
        
        return deleted