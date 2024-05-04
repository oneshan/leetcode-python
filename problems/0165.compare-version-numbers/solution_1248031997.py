# 0165 - Compare Version Numbers
# Date: 2024-05-03
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1248031997


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        len1, len2 = len(version1), len(version2)
        left1 = right1 = 0
        left2 = right2 = 0
        while left1 < len1 or left2 < len2:
            
            while right1 < len(version1) and version1[right1] != '.':
                right1 += 1
            v1 = int(version1[left1:right1]) if left1 < right1 else 0
            left1 = right1 = right1 + 1

            while right2 < len(version2) and version2[right2] != '.':
                right2 += 1
            v2 = int(version2[left2:right2]) if left2 < right2 else 0
            left2 = right2 = right2 + 1

            if v1 > v2:
                return 1
            if v1 < v2:
                return -1

        return 0