# 0412 - Fizz Buzz
# Date: 2022-07-11
# Runtime: 65 ms, Memory: 15.2 MB
# Submission Id: 743987498


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(idx+1) for idx in range(n)]
        for idx in range(1, n+1):
            if idx % 15 == 0:
                ans[idx-1] = "FizzBuzz"
            elif idx % 3 == 0:
                ans[idx-1] = "Fizz"
            elif idx % 5 == 0:
                ans[idx-1] = "Buzz"
        return ans
            