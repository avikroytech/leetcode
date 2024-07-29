class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num not in count.keys():
                count[num] = 1
            elif num in count.keys():
                count[num] += 1
        highestCount = 0
        number = 0
        for key, value in count.items():
            if value > highestCount:
                highestCount = value
                number = key
        if highestCount > len(nums)/ 2:
            return number