# 0301 - Remove Invalid Parentheses
# Date: 2024-06-20
# Runtime: 271 ms, Memory: 69.4 MB
# Submission Id: 1294363296


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def is_valid(s):
            n = len(s)

            left = right = 0
            for i in range(n):
                if s[i] == '(':
                    left += 1
                elif s[i] == ')':
                    right += 1
                if right > left:
                    return False

            for i in range(n-1, -1, -1):
                if s[i] == '(':
                    left += 1
                elif s[i] == ')':
                    right += 1
                if left > right:
                    return False

            return True

        
        res = []
        n = len(s)
        self.curr_min = float('inf')
        self.curr_ans = {''}

        @cache
        def recur(i, curr):

            if i >= n:
                if is_valid(curr):
                    print(''.join(curr))
                    if n-len(curr) < self.curr_min:
                        self.curr_min = n-len(curr)
                        self.curr_ans = {curr}
                    elif n-len(curr) == self.curr_min:
                        self.curr_ans.add(curr)
                return
            
            # delete
            if s[i] in {'(', ')'}:
                recur(i+1, curr)

            recur(i+1, curr+s[i])

        recur(0, '')
        return self.curr_ans