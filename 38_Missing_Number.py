class Solution(object):
    def missingNumber(self, nums):    
        if 0 not in nums: 
            return 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i] - 1
        return nums[-1] + 1