class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numJewels = 0

        for stone in stones:
            if stone in jewels:
                numJewels += 1
        
        return numJewels