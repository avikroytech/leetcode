class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []

        for char in s:
            if char.isalpha():
                if char.lower() in "aeiou":
                    vowels.append(char)

        vowels = vowels[::-1]
        s = [*s]

        for i in range(len(s)):
            if s[i].isalpha():
                if s[i].lower() in "aeiou":
                    s[i] = vowels.pop(0)

        return ''.join(s)