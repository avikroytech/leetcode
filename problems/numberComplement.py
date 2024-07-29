class Solution:
    def findComplement(self, num: int) -> int:
        binaryString = bin(num).replace("0b", "")

        for i in range(len(binaryString)):
            if binaryString[i] == "1":
                binaryString = binaryString[:i] + '0' + binaryString[i+1:]
            else:
                binaryString = binaryString[:i] + '1' + binaryString[i+1:]
        
        return int(binaryString, 2)