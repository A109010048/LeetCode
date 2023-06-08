class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max1 = 0
        cur = 0

        for i in nums:
            if i == 0:
                cur = 0
            else:
                cur += 1
            max1 = max(max1, cur)

        return max1