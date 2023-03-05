class Solution(object):
    def romanToInt(self, s):
        result = 0
        
        symbol = {'I' : 1,
                  'V' : 5,
                  'X' : 10,
                  'L' : 50,
                  'C' : 100,
                  'D' : 500,
                  'M' : 1000,                  
        }

        for i in range(len(s)):  
            if i > 0 and s[i] in symbol and s[i - 1] in symbol:                 
                if symbol[s[i]] <= symbol[s[i - 1]]:
                    result += symbol[s[i - 1]]
                else:
                    result -= symbol[s[i - 1]] 
        result += symbol[s[i]] 
                           

        return result