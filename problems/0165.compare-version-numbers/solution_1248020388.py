# 0165 - Compare Version Numbers
# Date: 2024-05-03
# Runtime: 38 ms, Memory: 16.6 MB
# Submission Id: 1248020388


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def parse(version):
            left = 0
            for right in range(len(version)):
                if version[right] == '.':
                    yield int(version[left:right])
                    left = right + 1
            yield int(version[left:] or '0')

        g1 = parse(version1)
        g2 = parse(version2)
        while True:
            n1 = next(g1, None)
            n2 = next(g2, None)
            if n1 is None and n2 is None:
                break
            if n1 is None:
                n1 = 0
            if n2 is None:
                n2 = 0
            if n1 > n2:
                return 1
            if n1 < n2:
                return -1
        return 0