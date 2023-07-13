class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
            
        result = ""

        pos = True
        if num < 0:
            pos = False

        num = abs(num)

        while num > 0:
            result += str(num % 7)
            num = num // 7

        if pos == False:
            result += "-"

        return result[::-1]