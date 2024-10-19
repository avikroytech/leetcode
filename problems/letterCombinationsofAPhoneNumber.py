class Solution:
    def recurs(self, digits, letterString):
        currDigit = digits[0]
        possibleLetters = self.digitsToLetters[currDigit]
        digits = digits[1:]
        possibleCombs = []

        for letter in possibleLetters:
            newLetterString = letter + letterString
            newLetters = [newLetterString]

            if len(digits) != 0:
                newLetters = self.recurs(digits, newLetterString)
            
            possibleCombs += newLetters

        return possibleCombs

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        self.digitsToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        digits = digits[::-1]

        possibleNumbers = self.recurs(digits, "")
        
        return possibleNumbers