def findNumeral(num, numerals):
    numeral = 1
    for key in numerals.keys():
        if key > num:
            break
        else:
            numeral = key
    
    return numeral

class Solution:
    def intToRoman(self, num: int) -> str:
        romanNumerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        converted = ""
        digits = []

        for i in range(0, len(str(num))):
            digits.append(int(str(num)[len(str(num)) - i - 1]) * (10**i))

        digits.reverse()

        for digit in digits:
            tempNum = digit
            digitConverted = ""
           
            while tempNum > 0:
                numeral = findNumeral(tempNum, romanNumerals)
                tempNum -= numeral
                digitConverted += romanNumerals[numeral]

            converted += digitConverted
    
        return converted
            