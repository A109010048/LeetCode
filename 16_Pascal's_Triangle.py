class Solution(object):
    def generate(self, numRows):

        sum = [[1]]
        for i in range(1, numRows):
            sum.append([1] * (i + 1))
            if i >= 2:
                for j in range(1, i):
                    sum[i][j] = sum[i - 1][j] + sum[i - 1][j - 1]
        return sum