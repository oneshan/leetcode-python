# 2263 - Maximum Running Time of N Computers
# Date: 2023-07-27
# Runtime: 2044 ms, Memory: 30.6 MB
# Submission Id: 1005403641


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def check(time):
            threshold = time * n
            total = 0
            for battery in batteries:
                total += min(time, battery)
                if total >= threshold:
                    return True
            return False
        
        left, right = 1, sum(batteries) // n
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left