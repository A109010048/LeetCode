class Solution(object):
    def deleteGreatestValue(self, grid):
        sum = 0
        max = 0
        for i in range(len(grid)):
            grid[i].sort()
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                reamin = grid[j].pop(-1)
                if reamin > max:
                    max = reamin 
            sum += max
            max = 0
        return sum