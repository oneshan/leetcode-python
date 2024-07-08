# 0301 - Remove Invalid Parentheses
# Date: 2024-06-20
# Runtime: 5817 ms, Memory: 16.9 MB
# Submission Id: 1294361654


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def is_valid(arr):
            n = len(arr)

            left = right = 0
            for i in range(n):
                if arr[i] == '(':
                    left += 1
                elif arr[i] == ')':
                    right += 1
                if right > left:
                    return False

            for i in range(n-1, -1, -1):
                if arr[i] == '(':
                    left += 1
                elif arr[i] == ')':
                    right += 1
                if left > right:
                    return False

            return True

        
        res = []
        n = len(s)
        self.curr_min = float('inf')
        self.curr_ans = {''}

        def recur(i, arr):
            if i >= n:
                if is_valid(arr):
                    print(''.join(arr))
                    if n-len(arr) < self.curr_min:
                        self.curr_min = n-len(arr)
                        self.curr_ans = {''.join(arr)}
                    elif n-len(arr) == self.curr_min:
                        self.curr_ans.add(''.join(arr))
                return
            
            # delete
            if s[i] in {'(', ')'}:
                recur(i+1, arr)

            arr.append(s[i])
            recur(i+1, arr)
            arr.pop()

        recur(0, [])
        return self.curr_ans