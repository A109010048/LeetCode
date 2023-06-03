class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False

        i = 1
        while i < len(arr):
            if arr[i] == arr[i - 1]:
                return False
            elif arr[i] < arr[i - 1]:
                break
            else:
                i += 1
        
        if i == 1 or i == len(arr):
            return False

        for j in range(i, len(arr)):
            if arr[j] >= arr[j - 1]:
                return False

        return True