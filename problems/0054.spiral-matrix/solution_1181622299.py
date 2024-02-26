# 0054 - Spiral Matrix
# Date: 2024-02-21
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1181622299


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        len_r, len_c = len(matrix), len(matrix[0])
        
        ans = []
        up, down = 0, len_r-1
        left, right = 0, len_c-1
        while len(ans) < len_r * len_c:
            # >
            for c in range(left, right+1):
                ans.append(matrix[up][c])
            # v
            for r in range(up+1, down+1):
                ans.append(matrix[r][right])
            # <
            if up != down:
                for c in range(right-1, left-1, -1):
                    ans.append(matrix[down][c])
            # ^
            if left != right:
                for r in range(down-1, up, -1):
                    ans.append(matrix[r][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return ans