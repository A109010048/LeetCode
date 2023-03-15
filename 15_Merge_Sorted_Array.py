class Solution(object):
    def merge(self, nums1, m, nums2, n):

        while len(nums1) > m:
            nums1.pop()
        nums1 += nums2

        for i in range(1,len(nums1)):
            j = i
            while nums1[j-1] > nums1[j] and j > 0:
                nums1[j-1], nums1[j] = nums1[j], nums1[j-1]
                j -= 1
        return nums1
