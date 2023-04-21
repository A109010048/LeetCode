class Solution(object):
    def reverseVowels(self, s):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s_list = list(s)
        remain = []
        for i in s_list:
            if i in vowels:
                remain.append(i)       
        remain.reverse()
        
        k = 0
        for j in range(len(s_list)):
            print(k)
            if s_list[j] in vowels:
                s_list[j] = remain[k]
                k += 1
        s = ''.join(s_list)

        return s