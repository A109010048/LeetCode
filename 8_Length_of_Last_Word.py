class Solution(object):
    def lengthOfLastWord(self, s):
        
        s_list = s.split(' ')
        w_list = []
        for i in range(len(s_list)):
            if s_list[i] != '':
                w_list.append(s_list[i])

        return len(w_list[-1])