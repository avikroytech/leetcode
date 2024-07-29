class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        segment = False

        s += " "

        for char in s:
            if char != " " and not segment:
                segment = True
            elif char == " ":
                if segment:
                    segments += 1
                    segment = False

        return segments