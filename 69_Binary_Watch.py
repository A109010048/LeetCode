class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []

        for i in range(12):
            binary = bin(i)
            hour = binary.count("1")
            for j in range(60):
                binary = bin(j)
                sum = binary.count("1") + hour

                if sum == turnedOn:
                    if j >= 10:
                        result.append(str(i) + ":" + str(j))
                    else:
                        result.append(str(i) + ":0" + str(j))
        
        return result