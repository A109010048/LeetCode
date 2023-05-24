class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = []
        nums.sort()
        cur = 1

        for i in range(len(nums)):
            if nums[i] < cur:
                continue
            else:
                if nums[i] != cur:
                    while nums[i] != cur:
                        result.append(cur)
                        cur += 1
                cur += 1
                
        while cur <= len(nums):
            result.append(cur)
            cur += 1

        return result