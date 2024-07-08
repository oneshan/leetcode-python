# 0681 - Next Closest Time
# Date: 2024-06-02
# Runtime: 30 ms, Memory: 16.5 MB
# Submission Id: 1274931050


class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = {int(t) for t in time if t != ':'}

        curr = 60 * int(time[:2]) + int(time[3:])
        day_minutes = 60 * 24

        while True:
            curr = (curr + 1) % day_minutes

            is_valid = True
            for block in divmod(curr, 60):
                for digit in divmod(block, 10):
                    if digit not in digits:
                        is_valid = False
                        break
            
            if is_valid:
                hour, minute = divmod(curr, 60)
                return f'{hour:02d}:{minute:02d}'