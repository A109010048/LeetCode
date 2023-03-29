class Solution(object):
    def isAnagram(self, s, t):
        s_list = list(s)
        if len(s) > len(t):
            return False
        for c in t:
            if c not in s_list:
                return False
            else:
                s_list.remove(c)
        return True