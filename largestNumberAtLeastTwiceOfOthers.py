class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        sortNums = sorted(nums)

        if sortNums[-1] >= sortNums[-2] * 2:
            return nums.index(sortNums[-1])
        else:
            return -1
