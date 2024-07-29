class Solution:
    def climbStairs(self, n: int) -> int:
        previousNumber, nextNumber = 0, 1
        count = 0
        combinations = 0

        while count < n:
            combinations = previousNumber + nextNumber
            previousNumber = nextNumber
            nextNumber = combinations
            count += 1
        
        return combinations