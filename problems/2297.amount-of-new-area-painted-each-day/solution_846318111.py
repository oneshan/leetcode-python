# 2297 - Amount of New Area Painted Each Day
# Date: 2022-11-19
# Runtime: 5384 ms, Memory: 66.2 MB
# Submission Id: 846318111


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        pid_to_end = {}   # {paint_id: end index}
        painted = {}  # {idx: paint_id}
        ans = [0] * len(paint)
        for pid, (ps, pe) in enumerate(paint):
            pid_to_end[pid] = pe
            count = 0
            while ps < pe:
                if ps in painted:
                    old_pe = pid_to_end[painted[ps]]
                    pid_to_end[painted[ps]] = max(pid_to_end[painted[ps]], pe)
                    ps = old_pe
                else:
                    painted[ps] = pid
                    count += 1
                    ps += 1
            ans[pid] = count
        return ans