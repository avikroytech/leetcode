class Solution:
	def removeDuplicates(self, nums: list[int]) -> int:
		i = 0
		while i != len(nums):
			if i == len(nums) - 1:
				break
			elif nums[i] == nums[i+1]:
				nums.remove(nums[i+1])
			else:
				i += 1
		return len(nums)