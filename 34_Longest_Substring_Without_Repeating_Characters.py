class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s = list(s)
        queue = []
        longest = 0
        for c in s:
            print(queue)
            print(c)
            if c not in queue:
                queue.append(c)
            else:
                while queue[0] != c:
                    queue.pop(0)
                if queue[0] == c:
                   queue.pop(0)
                   queue.append(c)                  
            longest = max(len(queue), longest)
        return longest