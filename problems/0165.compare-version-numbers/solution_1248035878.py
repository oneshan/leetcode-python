# 0165 - Compare Version Numbers
# Date: 2024-05-03
# Runtime: 42 ms, Memory: 16.4 MB
# Submission Id: 1248035878


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list_v1 = [int(v) for v in version1.split('.')]
        list_v2 = [int(v) for v in version2.split('.')]

        p1 = p2 = 0
        while p1 < len(list_v1) or p2 < len(list_v2):
            v1 = list_v1[p1] if p1 < len(list_v1) else 0
            v2 = list_v2[p2] if p2 < len(list_v2) else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            p1 += 1
            p2 += 1
        return 0