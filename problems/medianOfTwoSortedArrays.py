class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined_nums = nums1 + nums2
        combined_nums.sort()
        median = 0

        if len(combined_nums) % 2 == 0:
            median = int(len(combined_nums) / 2)
            median = (combined_nums[median] + combined_nums[median - 1]) / 2
        else:
            median = int(len(combined_nums) / 2 - 0.5)
            median = combined_nums[median]

        return median