class Solution:
    def mySqrt(self, number: int) -> int:
        if number == 0:
            return 0
        x = number / 2
        while True:
            y = (x + number / x) / 2
            if y == x:
                break
            x = y

        return int(x)