class Solution(object):
    def addStrings(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = 0
        n2 = 0
        
        for i in range(len(num1)):
            n1 += (ord(num1[i]) -  48) * (10 ** i)
        
        for i in range(len(num2)):
            n2 += (ord(num2[i]) -  48) * (10 ** i)

        return str(n1 + n2)