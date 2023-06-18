class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if duration != 0:
            if duration == 1:
                result = len(timeSeries)
            else:
                result = len(timeSeries) + duration - 1
        else:
            return 0

        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration - 1 < timeSeries[i + 1]:
                result += duration - 1
            else:
                result += timeSeries[i + 1] - timeSeries[i] - 1

        return result
