# 1320 - Remove All Adjacent Duplicates in String II
# Date: 2022-09-29
# Runtime: 307 ms, Memory: 18.8 MB
# Submission Id: 811324849


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            elif stack[-1][1] < k-1:
                stack[-1][1] += 1
            else:
                stack.pop()
        
        ans = ''
        for ch, count in stack:
            ans += ch * count
        return ans