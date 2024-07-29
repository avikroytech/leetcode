class Solution:
    def isValid(self, word: str) -> bool:
        validVowels = False
        validConsonants = False

        if len(word) < 3:
            return False
        
        for char in word:
            if not char.isalpha() and not char.isnumeric():
                return False
            elif char.lower() in 'aeiou':
                validVowels = True
            elif not char.isnumeric():
                validConsonants = True
        
        return validVowels and validConsonants