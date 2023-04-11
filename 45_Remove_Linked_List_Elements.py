# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        while head.val == val:
            head = head.next
            if head is None:
                return head

        temp = head

        while head is not None:
            if head.next is None:
                break
            if head.next.val != val:
                head = head.next
            else:
                if head.next.next is not None:
                    remain = head.next.next
                    head.next = remain
                else:
                    head.next = None

        head = temp
        return head
        