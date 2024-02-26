# 2297 - Amount of New Area Painted Each Day
# Date: 2022-10-23
# Runtime: 4554 ms, Memory: 61.1 MB
# Submission Id: 828588427


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        seen = {}
        ans = []
        for ps, pe in paint:
            count = 0
            while ps < pe:
                if ps in seen:
                    seen[ps], ps = max(seen[ps], pe), seen[ps]
                else:
                    seen[ps] = pe
                    count += 1
                    ps += 1
            ans.append(count)
        return ans