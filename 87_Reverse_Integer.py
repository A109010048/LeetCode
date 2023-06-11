class Solution(object):
    def reverse(self, x):
        x = str(x)
        power = 0
        result = 0
        pos = True

        for c in x:
            if c == "-":
                pos = False
                continue
            result += (ord(c) - 48) * (10 ** power)
            power += 1

        if pos == False:
            result = result - 2 * result

        if abs(result) > 2 ** 31:
            result = 0

        return result