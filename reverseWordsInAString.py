class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        words = []
        currentWord = ""

        for char in s:
            if char != " ":
                currentWord += char
            if char == " " and len(currentWord) > 0:
                words.append(currentWord)
                currentWord = ""
        
        words.reverse()

        newString = ""
        for i in range(len(words)):
            if i != len(words)-1:
                newString = newString + words[i] + ' '
            else:
                newString = newString + words[i]
        
        return newString