class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        currentNums = nums[0:k+1]

        duplicateCheck = set(currentNums)
        if len(duplicateCheck) < len(currentNums) and len(currentNums) == len(nums):
            return True
        elif len(duplicateCheck) == len(currentNums) and len(currentNums) == len(nums):
            return False

        for i in range(1, len(nums)-k+1):
            duplicateCheck = set(currentNums)
            if len(duplicateCheck) < len(currentNums):
                return True
            currentNums = nums[i:i+k+1]
        
        return False