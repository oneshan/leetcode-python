# 1605 - Minimum Number of Days to Make m Bouquets
# Date: 2024-06-19
# Runtime: 811 ms, Memory: 30.5 MB
# Submission Id: 1293001531


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def is_valid(day):
            count = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                else:
                    count = 0

                if count == k:
                    count = 0
                    bouquets += 1
                    if bouquets == m:
                        return True
            return False 

        res = -1
        left, right = 0, max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res