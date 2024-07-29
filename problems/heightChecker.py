class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        unexpected = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                unexpected += 1
        
        return unexpected