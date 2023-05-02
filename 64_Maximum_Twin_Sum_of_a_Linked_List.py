# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        n = [head.val]

        while head.next is not None:
            n.append(head.next.val)
            head = head.next
        
        max = 0
        i = 0
        j = -1
        while i < len(n) // 2 + 1:
            if n[i] + n[j] > max:
                max = n[i] + n[j]
            i += 1
            j -= 1
        
        return max