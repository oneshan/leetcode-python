# 0802 - K-th Smallest Prime Fraction
# Date: 2024-05-10
# Runtime: 56 ms, Memory: 16.8 MB
# Submission Id: 1254260657


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def check(mid):
            count = 0
            max_frac = [0, 0, 0]
            j = 1
            for i in range(n):
                while j < n and arr[i] > arr[j] * mid:
                    j += 1
                count += n - j
                if j < n and max_frac[0] < arr[i] / arr[j]:
                    max_frac = [arr[i] / arr[j], i, j]
            return count, max_frac

        left, right = 0, 1.0
        while left < right:
            mid = (left + right) / 2
            count, (_, i, j) = check(mid)
            if count < k:
                left = mid
            elif count > k:
                right = mid
            else:
                return [arr[i], arr[j]]
        return []