class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        conversion = {}
        if len(pattern) != len(words):
           return False 
        for m, n in zip(pattern, words):
            if m in conversion:
                if conversion[m] != n:
                    return False
            else:
                if n in conversion.values():
                    return False
                else:
                    conversion[m] = n
        return True