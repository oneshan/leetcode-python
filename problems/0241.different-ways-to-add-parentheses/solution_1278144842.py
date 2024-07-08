# 0241 - Different Ways to Add Parentheses
# Date: 2024-06-05
# Runtime: 31 ms, Memory: 17 MB
# Submission Id: 1278144842


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def caculate(op1, op2, operator):
            if operator == '+':
                return op1 + op2
            if operator == '-':
                return op1 - op2
            if operator == '*':
                return op1 * op2

        @cache
        def recur(left, right):
            if right - left + 1 <= 2:
                return [int(expression[left:right+1])]
            
            res = []
            for i in range(left, right):
                if expression[i] not in {'+', '-', '*'}:
                    continue
                
                for op1 in recur(left, i-1):
                    for op2 in recur(i+1, right):
                        res.append(caculate(op1, op2, expression[i]))
            return res

        return recur(0, len(expression)-1)