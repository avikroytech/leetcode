class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 0
        currentLine = 0

        for c in s:
            i = "abcdefghijklmnopqrstuvwxyz".index(c)

            if widths[i] + currentLine <= 100:
                currentLine += widths[i]
            else:
                lines += 1
                currentLine = widths[i]
        
        return [lines+1, currentLine]