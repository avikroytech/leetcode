class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        distances = []
        occurences = [i for i in range(len(s)) if s[i] == c]

        for i in range(len(s)):
            if s[i] == c:
                distances.append(0)
            else:
                minDistance = len(s)

                for index in occurences:
                    if abs(index-i) < minDistance:
                        minDistance = abs(index-i)

                distances.append(minDistance)
        
        return distances