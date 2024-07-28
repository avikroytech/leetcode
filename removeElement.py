class Solution:
	def removeElement(self, nums, val: int) -> int:
		isDone = False
		while not isDone:
			try:
				nums.remove(val)
			except:
				isDone = True
		return len(nums)