# 1904 - Second Largest Digit in a String
# Date: 2022-10-13
# Runtime: 83 ms, Memory: 13.9 MB
# Submission Id: 821656922


class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = None
        for ch in s:
            if not ch.isnumeric():
                continue
            num = int(ch)
            if num == first or num == second:
                continue
            if first is None or num > first:
                first, second = num, first
            elif second is None or num > second:
                second = num
        return second if second is not None else -1