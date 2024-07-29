class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvvbnm"]
        validWords = []
        for word in words:
            chars = ""

            for char in word:
                if char not in chars:
                    chars += char

            chars = chars.lower()

            for row in rows:
                valid = True

                for char in chars:
                    if char not in row:
                        valid = False
                        break
                if valid:
                    validWords.append(word)
                    break

        return validWords
