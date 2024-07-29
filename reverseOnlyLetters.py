class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        original = [*s]
        nonLetters = []

        for i in range(len(original)):
            if not original[i].isalpha():
                nonLetters.append([original[i],i])

        i = 0

        while i < len(s):
            if not s[i].isalpha():
                s = s[:i] + s[i+1:]
            else:
                i += 1
        
        s = s[::-1]

        while len(original) != len(s):
            index = nonLetters[0][1]
            s = s[:index] + nonLetters[0][0] + s[index:]
            nonLetters.pop(0)

        return s