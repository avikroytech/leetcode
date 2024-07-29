class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n_range = range(1,len(nums)+1)
        answer = []

        duplicate = None

        for num in nums:
            if nums.count(num) > 1:
                duplicate = num
                break
        
        answer.append(duplicate)

        answer.append(list(set(n_range) - set(nums))[0])

        return answer