class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        result = 0
        cur = 0
        
        for i in range(len(g)):
            for j in range(cur, len(s)):
                if s[j] >= g[i]:
                    result += 1
                    cur = j + 1
                    break
                if j == len(s) - 1:
                    return result
            
        return result
