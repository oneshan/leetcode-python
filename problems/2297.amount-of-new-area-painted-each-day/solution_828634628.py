# 2297 - Amount of New Area Painted Each Day
# Date: 2022-10-23
# Runtime: 2072 ms, Memory: 58.1 MB
# Submission Id: 828634628


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        pid_to_end = {}
        seen = {}
        ans = []
        for pid, (ps, pe) in enumerate(paint):
            pid_to_end[pid] = pe
            count = 0
            while ps < pe:
                if ps in seen:
                    old_pe = pid_to_end[seen[ps]]
                    pid_to_end[seen[ps]] = max(pid_to_end[seen[ps]], pe)
                    ps = old_pe
                else:
                    seen[ps] = pid
                    count += 1
                    ps += 1
            ans.append(count)
        return ans