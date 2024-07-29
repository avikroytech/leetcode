class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""

        for i in range(len(s)):
            j = i
            check = ""
            while j < len(s):
                if s[j] in check:
                    break
                else:
                    check += s[j]
                j += 1
            if len(check) > len(substring):
                substring = check
        
        return len(substring)
                