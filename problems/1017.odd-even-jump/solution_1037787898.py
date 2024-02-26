# 1017 - Odd Even Jump
# Date: 2023-09-02
# Runtime: 287 ms, Memory: 43.3 MB
# Submission Id: 1037787898


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # next-greater-number
        next_greater = [-1] * n        
        stack = []
        for i, num in sorted(enumerate(arr), key=lambda x: (x[1], x[0])):
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_greater[idx] = i
            stack.append(i)

        # next-smaller-number
        next_smaller = [-1] * n
        stack = []
        for i, num in sorted(enumerate(arr), key=lambda x: (-x[1], x[0])):
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)

        # recursion
        @cache
        def recur(idx, is_odd):
            if idx == n-1:
                return True
            if idx == -1:
                return False
            next_idx = next_greater[idx] if is_odd else next_smaller[idx]
            return recur(next_idx, not is_odd)
        
        return sum(recur(i, True) for i in range(n))