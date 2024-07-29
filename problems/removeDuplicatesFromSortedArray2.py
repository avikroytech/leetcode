class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicateIndexes = []
        duplicates = {}

        for i in range(len(nums)):
            if nums[i] in duplicates.keys():
                if duplicates[nums[i]] == 2:
                    duplicateIndexes.append(i)
                else:
                    duplicates[nums[i]] += 1
            else:
                duplicates[nums[i]] = 1
        
        for i in range(len(duplicateIndexes)):
            duplicate = nums[duplicateIndexes[i]-i]
            del nums[duplicateIndexes[i]-i]
            nums.append(duplicate)
            
        return len(nums)-len(duplicateIndexes)