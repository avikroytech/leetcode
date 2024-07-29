class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        wordSet = set(word)
        specialChars = 0

        for char in wordSet:
            if char.upper() == char:
                if char.lower() in wordSet:
                    specialChars += 1
        
        return specialChars