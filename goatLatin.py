class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()

        for i in range(len(words)):
            if words[i][0].lower() in 'aeiou':
                words[i] += "ma"
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"
            
            words[i] += "a" * (i+1)

        return ' '.join(words)