class Solution(object):
    def reverseStr(self, s, k):
        groups = []
        for i in range(0, len(s), k):
            group = s[i : i + k]
            groups.append(group)

        for i in range(0, len(groups), 2):
            groups[i] = groups[i][::-1]

        result = "".join(groups)
        return result