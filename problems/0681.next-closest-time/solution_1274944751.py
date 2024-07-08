# 0681 - Next Closest Time
# Date: 2024-06-02
# Runtime: 29 ms, Memory: 16.3 MB
# Submission Id: 1274944751


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = int(time[:2]), int(time[3:])
        digits = sorted(int(t) for t in time if t != ':')

        close_hour, close_minute = 24, 60
        for a in digits:
            for b in digits:
                num = 10 * a + b
                if num > minute and num < close_minute:
                    close_minute = num
                if num > hour and num < close_hour:
                    close_hour = num
        
        if close_minute < 60:
            return f'{hour:02d}:{close_minute:02d}'
        if close_hour < 24:
            return f'{close_hour:02d}:{digits[0]}{digits[0]}'
        return f'{digits[0]}{digits[0]}:{digits[0]}{digits[0]}'