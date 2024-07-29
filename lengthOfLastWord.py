class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        for char in s.split(" "):
            if char != "":
                words.append(char)
        return len(words[len(words)-1])