class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        if 0 not in nums:
            nums.append(0)
        
        nums[:] = sorted(list(set(nums)))

        positive = 1

        for num in nums[nums.index(0)+1:]:
            if num != positive:
                return positive
            else:
                positive += 1
        
        return nums[-1] + 1