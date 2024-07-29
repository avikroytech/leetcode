class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        peak = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                peak = i
        
        return peak