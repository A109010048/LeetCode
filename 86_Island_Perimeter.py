class Solution(object):
    def islandPerimeter(self, grid):
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i + 1 == len(grid):
                        result += 1
                    else:
                        if grid[i + 1][j] == 0:
                            result += 1

                    if i - 1 < 0:
                        result += 1
                    else:
                        if grid[i - 1][j] == 0:
                            result += 1
                    
                    if j + 1 == len(grid[i]):
                        result += 1
                    else:
                        if grid[i][j + 1] == 0:
                            result += 1

                    if j - 1 < 0:
                        result += 1
                    else:
                        if grid[i][j - 1] == 0:
                            result += 1

        return result