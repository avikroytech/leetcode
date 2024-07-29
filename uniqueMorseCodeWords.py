class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        alphabet = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }

        morseWords = []

        for word in words:
            morseWord = ""
            for c in word:
                morseWord += alphabet[c]

            morseWords.append(morseWord)
            
        uniqueMorse = {}

        for morse in morseWords:
            if morse in uniqueMorse.keys():
                uniqueMorse[morse] += 1
            else:
                uniqueMorse[morse] = 1
        
        return len(uniqueMorse.keys())