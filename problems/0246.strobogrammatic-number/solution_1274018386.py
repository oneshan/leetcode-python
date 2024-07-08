# 0246 - Strobogrammatic Number
# Date: 2024-06-01
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1274018386


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate = {'1' : '1', '6': '9', '8': '8', '9': '6', '0': '0'}

        left, right = 0, len(num)-1
        while left <= right:
            if num[left] not in rotate or num[right] not in rotate:
                return False
            if rotate[num[left]] != num[right] or rotate[num[right]] != num[left]:
                return False
            left += 1
            right -= 1
        
        return True