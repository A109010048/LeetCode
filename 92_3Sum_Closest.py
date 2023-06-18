class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == target:
                    return sum

                elif sum < target:
                    left += 1

                else:
                    right -= 1

                if abs(sum - target) < abs(result - target):
                    result = sum

        return result
