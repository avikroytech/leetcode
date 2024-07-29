class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}

        for char in s:
            if char in chars.keys():
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char, value in chars.items():
            if value == 1:
                return [*s].index(char)
        
        return -1