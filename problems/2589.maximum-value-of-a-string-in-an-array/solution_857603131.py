# 2589 - Maximum Value of a String in an Array
# Date: 2022-12-10
# Runtime: 30 ms, Memory: 13.9 MB
# Submission Id: 857603131


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs:
            value = len(s)
            num = 0
            for ch in s:
                if not ch.isdigit():
                    break
                num = num * 10 + int(ch)
            else:
                value = num
            ans = max(ans, value)
        return ans