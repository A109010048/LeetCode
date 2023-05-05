class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False

        cur = -1
        for c in s:
            for i in range(len(t)):
                if c == t[i]:
                    if i > cur:
                        cur = i
                        break
                if i == len(t) - 1:
                    return False
        
        return True