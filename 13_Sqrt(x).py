class Solution(object):
    def mySqrt(self, x):
        
        i = 1
        while i*i < x:
            i += 1
        if i*i == x:
            return i
        else:
            return i - 1