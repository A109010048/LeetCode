class Solution(object):
    def plusOne(self, digits):
        
        digits.reverse()
        for i in range(len(digits)):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
                else:
                    continue
        digits.reverse()

        return digits