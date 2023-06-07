class Solution(object):
    def findComplement(self, num):
        oriBin = bin(num)
        print(oriBin)
        newBin = ""

        for i in range(2, len(oriBin)):
            if oriBin[i] == "0":
                newBin += "1"
            elif oriBin[i] == "1":
                newBin += "0"

        result = int(newBin, 2)
        return result