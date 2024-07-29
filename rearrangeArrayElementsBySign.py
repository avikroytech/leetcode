class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        newArray = []
        for i in range(len(positives)):
            newArray.append(positives[i])
            newArray.append(negatives[i])
        
        return newArray