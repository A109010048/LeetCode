class Solution(object):
    def getRow(self, rowIndex):
        sum = [[1]]
        if rowIndex == 0:
            return sum[-1]
        for i in range(1, rowIndex + 1):
            sum.append([1] * (i + 1))
            if i >= 2:
                for j in range(1, i):
                    sum[i][j] = sum[i - 1][j] + sum[i - 1][j - 1]
        return sum[-1]