class Solution(object):
    def addBinary(self, a, b):
        a_list = [int(c) for c in a]
        b_list = [int(c) for c in b]
        a_list.reverse() 
        b_list.reverse() 
        if len(a_list) > len(b_list):
            d = len(a_list) - len(b_list)
            for k in range(d):
               b_list.append(0)
        elif len(a_list) < len(b_list):
            d = len(b_list) - len(a_list) 
            for k in range(d):
                a_list.append(0) 
        l = len(a_list)
        carry = 0
        merge = ""
        for i in range(l):
            m = a_list[i] + b_list[i] + carry
            if m < 2:
                merge += str(m)
                carry = 0
            else:
                merge += str(m % 2)
                carry = 1
        if carry == 1:
            merge += str(1)
        return merge[::-1]    