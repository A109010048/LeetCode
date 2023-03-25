class Solution(object):
    def isIsomorphic(self, s, t):
        conversion = {}
        for m, n in zip(s, t):
            if m in conversion:
                if conversion[m] != n:
                    return False
            else:
                if n in conversion.values():
                    return False
                conversion[m] = n
        return True