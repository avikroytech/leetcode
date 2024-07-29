class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) > 2:
            return nums[-3]
        else:
            return nums[-1]