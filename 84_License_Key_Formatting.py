class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s[::-1]
        result = ""
        cur = 0

        for c in s:
            if c == "-":
                continue
            if cur == k:
                result += "-"
                cur = 0
            result += c
            cur += 1

        result = result.upper()[::-1]
        return result