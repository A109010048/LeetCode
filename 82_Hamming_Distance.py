class Solution(object):
    def hammingDistance(self, x, y):
        result = 0
        binX = []
        binY = []
        
        while x >= 1:
            if x == 1:
                binX.append(1)
            else:
                binX.append(x % 2)
            x = x // 2

        while y >= 1:
            if y == 1:
                binY.append(1)
            else:
                binY.append(y % 2)
            y = y // 2

        if len(binX) > len(binY):
            binY += [0] * (len(binX) - len(binY))
        if len(binY) > len(binX):
            binX += [0] * (len(binY) - len(binX))

        for i, j in zip(binX, binY):
            if i != j:
                result += 1

        return result