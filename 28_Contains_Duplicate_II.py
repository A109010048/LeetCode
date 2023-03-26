class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        position = {}
        for i in range(len(nums)):
            if nums[i] not in position:
                position[nums[i]] = i
            else:
                if i - position[nums[i]] <= k:
                    return True
                else:
                    position[nums[i]] = i
        return False    
