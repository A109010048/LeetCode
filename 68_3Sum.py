class Solution(object):
    def threeSum(self, nums):
        result = []
        ans = []
        nums.sort()

        if nums[0] > 0:
            return result

        i = 0
        while nums[i] <= 0:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                if i >= len(nums):
                    break
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k and j < len(nums) and k > 0:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans =  [nums[i], nums[j], nums[k]]
                    if ans not in result:
                        result.append(ans)
                    ans = []
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

            i += 1
            
            if i >= len(nums):
                break

        return result