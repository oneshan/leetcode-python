# 0043 - Multiply Strings
# Date: 2024-05-22
# Runtime: 104 ms, Memory: 16.6 MB
# Submission Id: 1264846224


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n1 = len(num1)
        n2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]

        ans = [0] * (n1+n2)

        for i in range(n1):
            for j in range(n2):
                ans[i+j] += int(num1[i]) * int(num2[j])
                carry, ans[i+j] = divmod(ans[i+j], 10)
                if carry:
                    ans[i+j+1] += carry

        if ans[-1] == 0:
            ans.pop()
        
        return "".join(map(str, ans[::-1]))