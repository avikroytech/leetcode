class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        biggestLength = 0
        length = 0
        nums.sort()

        for i in range(len(nums)):
            if i != 0:
                if nums[i] != nums[i-1]+1 and nums[i] != nums[i-1]:
                    biggestLength = length if length > biggestLength else biggestLength
                    length = 0
                elif nums[i] == nums[i-1]:
                    length -= 1
            length += 1

        biggestLength = length if length > biggestLength else biggestLength
        
        return biggestLength
