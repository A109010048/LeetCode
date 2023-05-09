class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 1:
            return s
        
        result = ""
        for idx in range(numRows):
            i = 0
            while i < len(s):
                if idx == 0 or idx == numRows - 1:
                    if i * (2 * numRows - 2) + idx < len(s):
                        result += s[i * (2 * numRows - 2) + idx] 
                else:
                    if i == 0:
                        if idx < len(s):
                            result += s[idx]
                    else:
                        if i * (2 * numRows - 2) - idx < len(s):
                            result += s[i * (2 * numRows - 2) - idx]
                        if i * (2 * numRows - 2) + idx < len(s):
                            result += s[i * (2 * numRows - 2) + idx]
                i += 1

        return result