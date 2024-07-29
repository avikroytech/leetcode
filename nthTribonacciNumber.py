class Solution:
    def tribonacci(self, n: int) -> int:
        i = 2
        lastThreeNums = [0,1,1]

        if n < 3:
            return lastThreeNums[n]

        while i < n:
            currentNum = sum(lastThreeNums)
            lastThreeNums = lastThreeNums[1:] + [currentNum]
            i += 1
        
        return lastThreeNums[-1]