class Solution(object):
    def intersect(self, nums1, nums2):
        result = []

        for i in range(len(nums2)):
            if nums2[i] in nums1:
                result.append(nums2[i])
                nums1.remove(nums2[i])

        return result