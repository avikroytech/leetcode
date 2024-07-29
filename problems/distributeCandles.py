class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        types = len(set(candyType))
        candies = int(len(candyType) / 2)
        
        if types > candies:
            return candies
        else:
            return types