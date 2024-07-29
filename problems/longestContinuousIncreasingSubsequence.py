class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        longest = 0
        current = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                if current > longest:
                    longest = current
                current = 1
        
        if current > longest:
            longest = current
        
        return longest
