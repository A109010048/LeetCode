class Solution(object):
    def detectCapitalUse(self, word):
        if word.islower():
            return True
        else:
            if word.isupper():
                return True
            else:
                if word[0].islower():
                    return False
                else:
                    word = word[:0] + word[1:]
                    if word.islower():
                        return True
                    else:
                        return False