# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        seq = []
        while head is not None:
            seq.append(head.val)
            head = head.next

        del seq[-n]

        if len(seq) == 0:
            result = None
            return result

        result = ListNode(seq[0])
        temp = result
        for i in range(1, len(seq)):
            result.next = ListNode(seq[i])
            result = result.next

        return temp
