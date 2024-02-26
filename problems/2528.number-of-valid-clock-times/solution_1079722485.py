# 2528 - Number of Valid Clock Times
# Date: 2023-10-20
# Runtime: 33 ms, Memory: 16.3 MB
# Submission Id: 1079722485


class Solution:
    def countTime(self, time: str) -> int:
        
        hour_candidates = min_candidates = 1
        if time[0] == '?':
            if time[1] != '?' and time[1] > '3':
                hour_candidates = 2
            else:
                hour_candidates = 3
        
        if time[1] == '?':
            if time[0] == '2':
                hour_candidates *= 4
            else:
                hour_candidates *= 10
                        
        if time[3] == '?':
            min_candidates = 6
            
        if time[4] == '?':
            min_candidates *= 10
        
        hour_candidates = min(hour_candidates, 24)
        return hour_candidates * min_candidates