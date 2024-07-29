class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        childrenFed = 0
        g.sort()
        s.sort()

        for child in g:
            for i in range(len(s)):
                if s[i] >= child:
                    del s[:i+1]
                    childrenFed += 1
                    break

        return childrenFed