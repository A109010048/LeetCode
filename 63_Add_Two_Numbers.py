# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1 = [l1.val]
        n2 = [l2.val]

        while l1.next is not None:
            n1.append(l1.next.val)
            l1 = l1.next
        
        while l2.next is not None:
            n2.append(l2.next.val)
            l2 = l2.next
        
        num1 = 0
        for i in range(len(n1)):
            num1 += n1[i] * (10 ** i)

        num2 = 0
        for i in range(len(n2)):
            num2 += n2[i] * (10 ** i)

        sum = num1 + num2
        sum = list(str(sum))[::-1]

        pointer = ListNode(sum[0])
        temp = pointer
        for i in range(1, len(sum)):
            sum[i] = int(sum[i])
            pointer.next = ListNode(sum[i])  
            pointer = pointer.next

        return temp