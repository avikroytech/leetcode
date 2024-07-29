class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        