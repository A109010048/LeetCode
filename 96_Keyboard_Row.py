class Solution(object):
    def findWords(self, words):
        result = []
        first_row = ["qwertyuiop"]
        sec_row = ["asdfghjkl"]

        row = 0

        lowercase_words = [item.lower() for item in words]

        for i in range(len(lowercase_words)):
            for j in range(len(lowercase_words[i])):
                if lowercase_words[i][j] in first_row[0]:
                    if row == 0:
                        row = 1
                    elif row != 1:
                        row = 0
                        break
                elif lowercase_words[i][j] in sec_row[0]:
                    if row == 0:
                        row = 2
                    elif row != 2:
                        row = 0
                        break
                else:
                    if row == 0:
                        row = 3
                    elif row != 3:
                        row = 0
                        break
                if j == len(lowercase_words[i]) - 1:
                    result.append(words[i])
                    row = 0

        return result

        