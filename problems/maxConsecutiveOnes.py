class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxConsecutive = 0
        currentConsecutive = 0

        for num in nums:
            if num == 1:
                currentConsecutive += 1
                if currentConsecutive > maxConsecutive:
                    maxConsecutive = currentConsecutive
            else:
                currentConsecutive = 0

        return maxConsecutive
