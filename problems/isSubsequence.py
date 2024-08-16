class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target_index = 0
        found_letters = ""

        for char in t:
            if target_index >= len(s):
                break
            if char == s[target_index]:
                found_letters += char
                target_index += 1
        
        return found_letters == s