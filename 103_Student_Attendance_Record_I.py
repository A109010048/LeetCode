class Solution(object):
    def checkRecord(self, s):
        countA = s.count("A")

        if countA >= 2 or "LLL" in s:
            return False
        else:
            return True