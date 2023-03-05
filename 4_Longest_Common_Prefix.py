class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""

        for i in range(len(strs[0])):
            prefix = strs[0][i]
            for j in range(1, len(strs)) :
                if i ==len(strs[j]) or strs[j][i] != prefix:
                    return result
            result += prefix
        
        return result

        