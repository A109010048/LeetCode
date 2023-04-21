class Solution(object):
    def countBits(self, n):
        result = [0]
        count = 0
        for i in range(1, n + 1):
            while i != 0:
                if i % 2 == 1:
                    count += 1
                i = i // 2
            result.append(count)
            bin = []
            count = 0
        
        return result