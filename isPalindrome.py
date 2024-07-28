class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_reversed = str(x)[::-1]
        if x_reversed == str(x):
            return True
        return False