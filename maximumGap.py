class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums.sort()
        maxGap = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] > maxGap:
                maxGap = nums[i+1]-nums[i]
        
        return maxGap