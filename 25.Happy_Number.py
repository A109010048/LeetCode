class Solution(object):
    def isHappy(self, n):
        loop = []
        while n != 1:
            square = 0
            while n != 0:
                square += (n % 10) ** 2
                n = n // 10
            if square in loop:
                return False
            n = square
            loop.append(square)
        return True