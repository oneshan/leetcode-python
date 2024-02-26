# 0052 - N-Queens II
# Date: 2023-09-19
# Runtime: 51 ms, Memory: 16.2 MB
# Submission Id: 1053600445


class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(r, cols, diags, anti_diags):
            if r == n:
                return 1
            count = 0
            for c in range(n):
                curr_diag = r - c
                curr_anti_diag = r + c
                if c in cols or curr_diag in diags or curr_anti_diag in anti_diags:
                    continue
                    
                cols.add(c)
                diags.add(curr_diag)
                anti_diags.add(curr_anti_diag)
                
                count += backtrack(r+1, cols, diags, anti_diags)

                cols.discard(c)
                diags.discard(curr_diag)
                anti_diags.discard(curr_anti_diag)

            return count

        return backtrack(0, set(), set(), set())