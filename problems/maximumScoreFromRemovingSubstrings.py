class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        higher_points = max([x,y])
        first_check = ""
        first_points = 0
        second_check = ""
        second_points = 0

        if higher_points == x:
            first_check = "ab"
            first_points = x
            second_check = "ba"
            second_points = y
        else:
            first_check = "ba"
            first_points = y
            second_check = "ab"
            second_points = x

        points = 0
        i = 1

        while i < len(s):
            if s[i-1:i+1] == first_check:
                points += first_points
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1

        i = 1
        
        while i < len(s):
            if s[i-1:i+1] == second_check:
                points += second_points
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
        
        return points