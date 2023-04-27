class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        
        dic = []
        dic = list(magazine)
        for c in ransomNote:
            for i in range(len(dic)):
                if c == dic[i]:
                    dic.remove(dic[i])
                    break
                if i == len(dic) - 1:
                    return False
        
        return True