class Solution:
    def addBinary(self, a: str, b: str) -> str:
        reversedA = a[::-1]
        reversedB = b[::-1]
    
        if len(reversedA) < len(reversedB):
            for i in range(len(reversedB) - len(reversedA)):
                reversedA += "0"
    
        if len(reversedA) > len(reversedB):
            for i in range(len(reversedA) - len(reversedB)):
                reversedB += "0"
        
        total = ""
        carry = 0
        
        for i in range(len(reversedA)):
            bitA = int(reversedA[i])
            bitB = int(reversedB[i])
            if bitA + bitB + carry == 2:
                carry = 1
                total += "0"
            elif bitA + bitB + carry == 3:
                carry = 1
                total += "1"
            elif bitA + bitB + carry == 0:
                carry = 0
                total += "0"
            else:
                carry = 0
                total += "1"
    
        if carry == 1:
            total += "1"
        
        return total[::-1]