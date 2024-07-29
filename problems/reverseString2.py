class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reversedString = s
        i = 0

        while i < len(s):
            section = s[i:k*2+i]
            section = section[0:k][::-1] + section[k:]
            reversedString = reversedString[0:i] + section + reversedString[len(section)+i:]
            i += 2*k
        
        return reversedString