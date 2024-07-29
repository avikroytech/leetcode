class Solution:
    def merge(self, intervals):
        intervals.sort()
        mergedIntervals = []
        currentInterval = intervals[0]

        for interval in intervals:
            intersection = range(max(currentInterval[0], interval[0]), min(currentInterval[-1], interval[-1])+1)

            if len(intersection) != 0:
                allIntervals = interval + currentInterval
                currentInterval = [min(allIntervals), max(allIntervals)]
            else:
                mergedIntervals.append(currentInterval)
                currentInterval = interval
        
        mergedIntervals.append(currentInterval)
        
        return mergedIntervals