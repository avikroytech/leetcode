class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n).replace("0b", "")
        set_bits = 0

        for bit in binary:
            if bit == "1":
                set_bits += 1
        
        return set_bits