class Solution(object):
    def output(self, start, end):
        if start == end:
            return str(end)
        else:
            return str(start) + "->" + str(end)
    def summaryRanges(self, nums):
        result = []
        if len(nums) == 0:
            return result
        else:
            start, end = nums[0], nums[0]
            for i in range(len(nums)):
                if i == len(nums) - 1:
                    end = nums[-1]
                    result.append(self.output(start, end))
                else:
                    if nums[i] + 1 == nums[i + 1]:
                        continue
                    else:
                        end = nums[i]
                        result.append(self.output(start, end))
                        start = nums[i + 1]
        return result