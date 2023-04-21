# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        seq = []
        while head.next is not None:
            seq.append(head.val)
            head = head.next
        seq.append(head.val)
        backward = seq[::-1]
        return seq == backward
