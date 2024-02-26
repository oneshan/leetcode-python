# 0374 - Guess Number Higher or Lower
# Date: 2022-11-16
# Runtime: 43 ms, Memory: 13.9 MB
# Submission Id: 844611164


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while True:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res > 0:
                left = mid + 1
            else:
                right = mid - 1