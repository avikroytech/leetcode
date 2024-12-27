class Solution:
    def countBits(self, n: int) -> list[int]:
        bitCount = []

        for i in range(n+1):
            binary = bin(i)[2:]
            bitCount.append(binary.count('1'))

        return bitCount