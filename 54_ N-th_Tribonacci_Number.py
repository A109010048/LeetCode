class Solution(object):
    def __init__(self):
        self.T = [-1] * 38
        self.T[0] = 0
        self.T[1] = 1
        self.T[2] = 1

    def tribonacci(self, n):
        if n >= 3:
            if self.T[n] == -1:
                self.T[n] = self.tribonacci(n - 1) +  self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.T[n]
        