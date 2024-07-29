class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        poisonSeconds = 0
        poisonDuration = [timeSeries[0], timeSeries[0]+duration-1]

        for time in timeSeries:
            if time in range(poisonDuration[0], poisonDuration[1]+1):
                poisonSeconds += time-poisonDuration[0]
                poisonDuration = [time, time+duration-1]
            else:
                poisonSeconds += poisonDuration[1]-poisonDuration[0]+1
                poisonDuration = [time, time+duration-1]
        
        poisonSeconds += poisonDuration[1]-poisonDuration[0]+1

        return poisonSeconds