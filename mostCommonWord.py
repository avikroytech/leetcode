class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        wordFrequency = {}
        word = ""
        paragraph += " "

        for char in paragraph:
            if char.isalpha():
                word += char
            else:
                if word.isalpha():
                    if word.lower() in wordFrequency.keys():
                        wordFrequency[word.lower()] += 1
                    else:
                        wordFrequency[word.lower()] = 1

                word = ""

        words = list(wordFrequency.keys())

        for word in banned:
            if word in words:
                words.remove(word)

        highest = 0
        commonWord = ""

        for word in words:
            if wordFrequency[word] > highest:
                commonWord = word
                highest = wordFrequency[word]

        return commonWord
