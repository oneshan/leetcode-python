# 0378 - Kth Smallest Element in a Sorted Matrix
# Date: 2022-10-20
# Runtime: 431 ms, Memory: 18.8 MB
# Submission Id: 826579748


import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        len_r, len_c = len(matrix), len(matrix[0])

        def countLessOrEqual(x):
            count = 0
            c = len_c - 1
            for r in range(len_r):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1  # decrease column until matrix[r][c] <= x
                count += (c + 1)
            return count

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans