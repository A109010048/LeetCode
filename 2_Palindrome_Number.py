class Solution(object):
    def isPalindrome(self, x):
        ind_num = str(x)
        left = 0
        right = len(ind_num) - 1
        while left < right:
            if ind_num[left] != ind_num[right]:
                return False
            else:
                left += 1
                right -= 1
        return True