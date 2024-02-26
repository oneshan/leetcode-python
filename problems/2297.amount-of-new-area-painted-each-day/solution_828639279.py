# 2297 - Amount of New Area Painted Each Day
# Date: 2022-10-23
# Runtime: 5098 ms, Memory: 58.4 MB
# Submission Id: 828639279


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
                    max_end = max(pid_to_end[painted[ps]], pid_to_end[pid])
                    pid_to_end[pid] = pid_to_end[painted[ps]] = max_end
                    ps = old_pe
                else:
                    painted[ps] = pid
                    count += 1
                    ps += 1
            ans.append(count)
        return ans