class Solution:
    def isHappy(self, n: int) -> bool:
        digits = list(str(n))

        n = 0
        for digit in digits:
            n += int(digit)**2

        if n == 1:
            return True
        elif n == 7:
            return True
        elif n < 10:
            return False
        else:
            return self.isHappy(n)