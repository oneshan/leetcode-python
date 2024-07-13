# 1298 - Reverse Substrings Between Each Pair of Parentheses
# Date: 2024-07-11
# Runtime: 34 ms, Memory: 16.6 MB
# Submission Id: 1317045558


class Solution:
    def reverseParentheses(self, s: str) -> str:

        def reverse(arr):
            left, right = 0, len(arr)-1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr

        stack = [[]]
        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                arr = stack.pop()
                stack[-1].extend(reverse(arr))
            else:
                stack[-1].append(ch)

        return ''.join(stack[-1])