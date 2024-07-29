class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            index = int(str(len(nums)/2)[0])
            while nums[index] != target:
                if target < nums[index]:
                    index = int(len(nums[:index])/2)+index
                else:
                    index = int(len(nums[index+1:])/2)+index
            
            return index
        else:
            return -1