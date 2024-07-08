# 1858 - Latest Time by Replacing Hidden Digits
# Date: 2024-06-01
# Runtime: 34 ms, Memory: 16.4 MB
# Submission Id: 1273916722


class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        # minute
        if time[4] == '?':
            time[4] = '9'
        if time[3] == '?':
            time[3] = '5'

        # hour
        if time[1] == '?':
            if time[0] == '?':
                time[0], time[1] = '2', '3'
            elif time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'

        if time[0] == '?':
            if int(time[1]) < 4:
                time[0] = '2'
            else:
                time[0] = '1'
        
        return ''.join(time)