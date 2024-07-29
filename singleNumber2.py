class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        singleNumber = None

        nums.sort()

        for i in range(len(nums)):
            if i > 0:
                if i < len(nums)-1:
                    if nums[i+1] != nums[i] and nums[i-1] != nums[i]:
                        singleNumber = nums[i]
                else:
                    if nums[i-1] != nums[i]:
                        singleNumber = nums[i]
            else:
                if nums[i+1] != nums[i]:
                    singleNumber = nums[i]
        
        return singleNumber