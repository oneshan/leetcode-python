# 0150 - Evaluate Reverse Polish Notation
# Date: 2024-01-30
# Runtime: 63 ms, Memory: 17.1 MB
# Submission Id: 1160614949


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for op in tokens:
            if op not in {'+', '-', '*', '/'}:
                nums.append(int(op))
                continue
                
            n2, n1 = nums.pop(), nums.pop()
            if op == '+':
                num = n1 + n2
            elif op == '-':
                num = n1 - n2
            elif op == '*':
                num = n1 * n2
            else:
                # NOTE: 6 // -132 = -1
                num = int(n1 / n2)
            nums.append(num)
            
        return nums[0]