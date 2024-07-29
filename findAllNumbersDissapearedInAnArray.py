class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        disappeared = list(set(range(1,len(nums)+1))-set(nums))
        
        return disappeared