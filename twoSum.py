class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                if nums[index] + nums[index2] == target:
                    return [index, index2]

# Test cases:

assert Solution().twoSum([2,7,11,15], 9) == [0,1]
assert Solution().twoSum([3,2,4], 6) == [1,2]
assert Solution().twoSum([3,3], 6) == [0,1]