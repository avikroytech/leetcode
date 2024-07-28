class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        raw_sum = dividend/divisor
        truncated_sum = int(raw_sum)
        if truncated_sum > 2**31 - 1:
            truncated_sum = 2**31-1
        if truncated_sum < -2**31:
            truncated_sum = 2**31-1
        return truncated_sum
        