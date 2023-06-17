class Solution(object):
    def myAtoi(self, s):
        result = ""
        cur = ""
        pos = ""
        
        if not any(char.isalpha() or char == '.' for char in s):
            for i in range(len(s)):
                if s[i] in ["-", "+"]:
                    if result != "":
                        break
                    pos += s[i]
                        
                if s[i].isdigit():
                    result += s[i]

                if s[i] == " " and (result != "" or pos != ""):
                    break

        else:
            for i in range(len(s)):
                if result == "" and s[i].isalpha():
                    return 0

                if s[i] in ["-", "+"]:
                    if result != "":
                        break
                    pos += s[i]
                
                if s[i].isdigit():
                    cur += s[i]
                    if i != len(s) - 1:
                        if not s[i + 1].isdigit():
                            result += cur
                            cur = ""
                            break

        if len(pos) > 1: 
            return 0

        if result == "":
            result = 0
        else:
            result = int(result)

        if "-" in pos:
            result = -result

        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        if result < -(2 ** 31):
            result = -(2 ** 31)
            
        return result