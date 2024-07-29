class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word[0].islower():
            return False

        for i in range(1,len(word)):
            if not word[i].islower():
                return False
        
        return True