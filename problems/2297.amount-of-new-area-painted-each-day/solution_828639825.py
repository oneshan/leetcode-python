# 2297 - Amount of New Area Painted Each Day
# Date: 2022-10-23
# Runtime: 4955 ms, Memory: 66.1 MB
# Submission Id: 828639825


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        pid_to_end = {}   # {paint_id: end index}
        painted = {}  # {idx: paint_id}
        ans = []
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
            ans.append(count)
        return ans