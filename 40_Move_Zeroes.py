class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
        while 0 in nums:
            nums.remove(0)
        while len(nums) < l:
            nums.append(0)
        return nums