class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 1
        while power <= n:
            if power == n:
                return True
            power = power * 3
        
        return False