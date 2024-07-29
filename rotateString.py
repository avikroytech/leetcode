class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if set(goal) != set(s):
            return False

        original = s
        i = 0

        while s != goal:
            if i > 0 and s == original:
                return False
            
            s = s[1:] + s[0]
            i += 1
        
        return True