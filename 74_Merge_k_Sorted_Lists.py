# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        seq = []
        for i in range(len(lists)):
            head = lists[i]
            while head is not None:
                seq.append(head.val)
                head = head.next
        
        if len(seq) == 0:
            merge = None
            return merge

        seq.sort()

        merge = ListNode(seq[0])
        temp = merge
        for i in range(1, len(seq)):
            merge.next = ListNode(seq[i])
            merge = merge.next

        return temp