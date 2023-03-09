class Solution(object):
    def strStr(self, haystack, needle):
        l = len(needle)
        for i in range(len(haystack) - ((len(needle)) - 1)):
            s = ''
            for j in range(i, len(haystack)):
                s += haystack[j]
                if len(s) == len(needle):
                    break
            if s == needle:
                return i
            else:
                continue
        
        return -1