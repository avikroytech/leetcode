class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        for num in nums1:
            if num in nums2:
                return num
        
        return -1