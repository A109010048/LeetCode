class Solution(object):
    def findTheDifference(self, s, t):
        remain = list(s)
        for i in t:
            if i not in remain:
                return i
            else:
                remain.remove(i)
        