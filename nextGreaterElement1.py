class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextGreater = []

        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            original = len(nextGreater)

            for num in nums2[j+1:]:
                if num > nums1[i]:
                    nextGreater.append(num)
                    break
            
            if len(nextGreater) == original:
                nextGreater.append(-1)
        
        return nextGreater