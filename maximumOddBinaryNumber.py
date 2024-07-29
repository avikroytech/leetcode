class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        maxOdd = ""
        newNum = s.replace('1', '', 1)
        for char in newNum:
            if char == '1':
                maxOdd = char + maxOdd
            else:
                maxOdd += char
        return maxOdd + '1'