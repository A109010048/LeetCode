class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(len(s) // 2):
            cur = s[: i + 1]
            word = s.replace(cur, "")
            if word == "":
                return True
            
        return False