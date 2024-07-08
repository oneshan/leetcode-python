# 0246 - Strobogrammatic Number
# Date: 2024-06-01
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1274016208


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {'1' : '1', '6': '9', '8': '8', '9': '6', '0': '0'}

        if len(num) > 1 and num[-1] == '0':
            return False

        rotated = []
        for ch in num:
            if ch not in mapping:
                return False
            rotated.append(mapping[ch])
        
        return ''.join(rotated[::-1]) == num