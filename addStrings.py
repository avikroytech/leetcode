class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ''

        if len(num1) < len(num2):
            for i in range(0, len(num2) - len(num1)):
                num1 = '0' + num1

        elif len(num2) < len(num1):
            for i in range(0, len(num1) - len(num2)):
                num2 = '0' + num2

        for i in range(0, len(num1)):
            index = len(num1) - i - 1

            add1 = num1[index]
            add2 = num2[index]
            total = str(int(add1) + int(add2) + carry)
            
            if int(total) > 9:
                carry = int(total[:-1])
                total = total[-1]
            else:
                carry = 0

            result = total + result
        
        if carry > 0:
            result  = str(carry) + result

        return result
