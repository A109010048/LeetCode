class Solution(object):
    def arrangeCoins(self, n):
        i = 0
        sum = 0
        while sum < n:
            i += 1
            sum += i

        if n == sum:
            return i
        else:
            return i - 1