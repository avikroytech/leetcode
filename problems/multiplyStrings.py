def convertToInt(num):
    numberInt = 0
    digits = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

    for i in range(len(num)):
        placeValue = 10**i
        numberInt += placeValue * digits[num[len(num)-i-1]]
    
    return numberInt

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(convertToInt(num1) * convertToInt(num2))