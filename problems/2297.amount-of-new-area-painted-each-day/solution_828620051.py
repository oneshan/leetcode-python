# 2297 - Amount of New Area Painted Each Day
# Date: 2022-10-23
# Runtime: 7931 ms, Memory: 60.9 MB
# Submission Id: 828620051


from sortedcontainers import SortedList

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        records = []
        n = len(paint)
        for paint_id, (start, end) in enumerate(paint):
            records.append((start, paint_id, True))
            records.append((end, paint_id, False))
        records.sort()

        paint_ids = SortedList()
        ans = [0] * n
        last_pos = 0
        for pos, paint_id, is_start in records:
            if paint_ids:
                ans[paint_ids[0]] += (pos - last_pos)
            last_pos = pos
            if is_start:
                paint_ids.add(paint_id)
            else:
                paint_ids.remove(paint_id)

        return ans
