class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        letters = []

        for char in licensePlate:
            if char.isalpha():
                letters.append(char.lower())
        
        shortest = ""

        for word in words:
            check = letters.copy()

            for char in word:
                if char in check:
                    check.remove(char)

            if len(check) == 0:
                if len(shortest) == 0 or len(word) < len(shortest):
                    shortest = word

        return shortest