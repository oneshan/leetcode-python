# 0551 - Student Attendance Record I
# Date: 2024-05-26
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1268163780


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = late = 0
        for ch in s:
            if ch == 'L':
                late += 1
                if late == 3:
                    return False
                continue
            late = 0

            if ch == 'A':
                absent += 1
                if absent == 2:
                    return False
        return True