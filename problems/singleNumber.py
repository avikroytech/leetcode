class Solution(object):
    def singleNumber(self, nums):
        single = []
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.append(num)
        return single[0]
        