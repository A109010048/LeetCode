class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums = nums[::-1]
        rank = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                rank.append(nums[i])
            if len(rank) == 3:
                return rank[2]

        return nums[0]