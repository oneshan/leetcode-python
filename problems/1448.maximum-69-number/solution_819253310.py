# 1448 - Maximum 69 Number
# Date: 2022-10-10
# Runtime: 37 ms, Memory: 13.8 MB
# Submission Id: 819253310


class Solution:
    def maximum69Number (self, num: int) -> int:
        lst = list(str(num))
        for i in range(len(lst)):
            if lst[i] == '6':
                lst[i] = '9'
                break
        return int(''.join(lst))