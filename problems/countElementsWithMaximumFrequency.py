class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        maxFrequency = 0
        frequencies = {}
        for num in nums:
            if num not in frequencies.keys():
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        for frequency in frequencies.values():
            if frequency > maxFrequency:
                maxFrequency = frequency
        
        totalFrequencies = 0

        for frequency in frequencies.values():
            if frequency == maxFrequency:
                totalFrequencies += frequency
        
        return totalFrequencies