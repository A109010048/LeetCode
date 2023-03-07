class Solution(object):
    def isValid(self, s):
        OpenBrackets = {'(' : ')',
                        '{' : '}',
                        '[' : ']'
        }

        if len(s) % 2 != 0:
            return False

        s_list = list(s)
        stack = [s[0]]
        for i in range(1, len(s_list)):
            if stack != []:
                current = s_list[i] 
                pop = stack.pop()
                if pop not in OpenBrackets or current != OpenBrackets[pop]:
                    stack.append(pop)
                    stack.append(current)
            else:
                stack.append(s_list[i])

        if stack == []:
            return True
        else:
            return False
