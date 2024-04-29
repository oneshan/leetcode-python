# 0514 - Freedom Trail
# Date: 2024-04-28
# Runtime: 221 ms, Memory: 17.5 MB
# Submission Id: 1244158253


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        @cache
        def recur(ri, ki):
            if ki == len(key):
                return 0
            
            res = float('inf')
            for idx, ch in enumerate(ring):
                if ch == key[ki]:
                    min_dist = min(
                        abs(idx-ri),
                        len(ring) - abs(idx-ri),
                    )
                    res = min(res, min_dist + 1 + recur(idx, ki+1))

            return res

        return recur(0, 0)