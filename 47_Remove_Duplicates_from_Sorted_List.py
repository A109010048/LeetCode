# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temp = head
        prev, curr = head, head.next
        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        if prev.next is not None:
            prev.next = None
        return temp
            