# 2297 - Amount of New Area Painted Each Day
# Date: 2022-10-23
# Runtime: 2152 ms, Memory: 67.2 MB
# Submission Id: 828629971


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
                    old_pid, old_pe = seen[ps], pid_to_end[seen[ps]]
                    pid_to_end[old_pid] = max(pid_to_end[old_pid], pe)
                    seen[ps] = pid
                    ps = old_pe
                else:
                    seen[ps] = pid
                    count += 1
                    ps += 1
            ans.append(count)
        return ans