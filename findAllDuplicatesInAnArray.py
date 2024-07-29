from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        counter1 = Counter(nums)
        counter2 = Counter(range(1,len(nums)+1))

        result = list((counter1 - counter2).elements())

        return result
