class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        max_sum = 0
        nums.sort()

        i = 0
        while i < len(nums):
            max_sum += nums[i]
            i += 2
        
        return max_sum