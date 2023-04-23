class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        nums = [nums1[0]]
        result = []
        for i in range(1, len(nums1)):
            if nums1[i] != nums1[i - 1]:
                nums.append(nums1[i])

        for j in range(len(nums2)):
            if j != 0:
                if nums2[j] == nums2[j - 1]:
                    continue
            if nums2[j] in nums:
                result.append(nums2[j])

        return result