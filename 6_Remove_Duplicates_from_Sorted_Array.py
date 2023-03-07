class Solution(object):
    def removeDuplicates(self, nums):
        
        
        j = 1
        for i in range(len(nums)):
            if j < len(nums):
                while nums[j] == nums[i]:
                    j += 1
                    if j >= len(nums):
                        break
                if j >= len(nums):
                    break
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                j += 1
            else:
                break

        i += 1
        k = i

        return k