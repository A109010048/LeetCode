class Solution(object):
    def __init__(self):
        self.record = [0] * 46

        self.record[1] = 1
        self.record[2] = 2
    
    def climbStairs(self, n):       
        if n > 2:
            if self.record[n] == 0:
                self.record[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.record[n]