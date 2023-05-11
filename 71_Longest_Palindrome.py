class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        single = False
        pairs = 0
        for i in count.values():
            if i % 2 != 0:
                single = True
            pairs += (i // 2) * 2
        
        if single == True:
            pairs += 1
        
        return pairs