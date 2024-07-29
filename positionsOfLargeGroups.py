class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        largeGroups = []
        start = 0

        for i in range(len(s)):
            if s[i] != s[start]:
                if i-start >= 3:
                    largeGroups.append([start,i-1])
                start = i
        
        if len(s[start:len(s)]) >= 3:
            largeGroups.append([start, len(s)-1])
        
        return largeGroups