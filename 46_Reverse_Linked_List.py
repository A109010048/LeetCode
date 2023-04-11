# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        nums = []
        temp = head
        while head is not None:
            nums.append(head.val)
            head = head.next
        nums = nums[::-1]
        head = temp
        head.val = nums[0]
        temp = head
        for i in range(1, len(nums)):
            head = head.next
            head.val = nums[i]

        return temp
