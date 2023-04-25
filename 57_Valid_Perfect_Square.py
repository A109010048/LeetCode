class Solution(object):
    def isPerfectSquare(self, num):
        squ = 0
        i  = 1
        while squ < num:
            squ = i ** 2
            if squ == num:
                return True
            i += 1
        return False