class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = bin(n)[2:]

        if len(bit_str) < 32:
            bit_str = "0" * (32-len(bit_str)) + bit_str

        reversed_bit_str = bit_str[::-1]
        return int(reversed_bit_str, 2)