class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = {}
        duplicate = False
        for num in nums:
            if num in numbers.keys():
                numbers[num] += 1
            else:
                numbers[num] = 1
        for key, value in numbers.items():
            if value > 1:
                duplicate = True
        return duplicate