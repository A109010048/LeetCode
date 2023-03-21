class Solution(object):
    def majorityElement(self, nums):
        
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        times = 1
        max_times = 1
        current = 0
        for i in range(1,len(nums)):
            if nums[i] == nums [i - 1]:
                times += 1
                if times > max_times:
                    max_times = times
                    current = nums[i]
            else:
                times = 1

        return current
