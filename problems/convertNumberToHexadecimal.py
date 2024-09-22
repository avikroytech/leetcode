class Solution:
    def toHex(self, num: int) -> str:
        digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']

        if num == 0:
            return '0'

        if num < 0:
            binary = bin(num)[3:]
            binary = list("0" * (32 - len(binary)) + binary)

            for i in range(len(binary)):
                if binary[i] == '1':
                    binary[i] = '0'
                else:
                    binary[i] = '1'

            num = int('0b' + ''.join(binary), 2) + 1

        quotient = num
        remainders = []

        while quotient > 0:
            remainder = quotient % 16
            quotient = quotient // 16

            remainders.insert(0, remainder)

        converted_str = ""

        for remainder in remainders:
            converted_str += str(digits[remainder])

        return converted_str
