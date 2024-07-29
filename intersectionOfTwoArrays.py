class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) < len(nums2):
            shorterList = nums1
            longerList = nums2
        else:
            shorterList = nums2
            longerList = nums1

        intersections = []
        
        for num in shorterList:
            if num in longerList and num not in intersections:
                intersections.append(num)
            
        return intersections