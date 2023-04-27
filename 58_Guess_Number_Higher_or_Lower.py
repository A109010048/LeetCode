# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        pick = (left + right) // 2

        while guess(pick) != 0:
            if guess(pick) == 1:
                if left != pick:
                    left = pick
                else:
                    pick += 1
                    continue
            else:
                right = pick
            pick = (left + right) // 2

        return pick