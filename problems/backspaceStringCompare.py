class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0

        while i < len(s):
            if s[i] == "#":
                s = s[: i - 1] + s[i + 1 :]
                i -= 1
            else:
                i += 1

        i = 0

        while i < len(t):
            if t[i] == "#":
                t = t[: i - 1] + t[i + 1 :]
                i -= 1
            else:
                i += 1

        return s == t
