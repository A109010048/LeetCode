class Solution(object):
    def titleToNumber(self, columnTitle):
        number = 0
        columnTitle = columnTitle[::-1]
        multipier = 1
        for c in columnTitle:
           number += (ord(c) - ord('A') + 1) * multipier
           multipier *= 26
        return number