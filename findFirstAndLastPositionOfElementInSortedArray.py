class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        indexes = []
        try:
            indexes.append(nums.index(target))
            indexes.append(len(nums) - 1 - nums[::-1].index(target))
        except:
            indexes = [-1, -1]

        return indexes