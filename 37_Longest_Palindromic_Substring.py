class Solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        longest = 0
        result = ""
        for i in range(len(s)):
            ans = s[i]
            for j in range(i + 1, len(s)):
                ans += s[j]
                if ans == ans[::-1]:
                    if longest < len(ans):
                        longest = len(ans)
                        result = ans
        if result == "":
            result += s[0]
        return result 
                 