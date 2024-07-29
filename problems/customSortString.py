class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderedString = ""

        for orderedChar in order:
            i = 0
            while i < len(s):
                if s[i] == orderedChar:
                    orderedString += s[i]
                    s = s[:i] + s[i+1:]
                else:
                    i += 1
        
        return orderedString + s
        
        