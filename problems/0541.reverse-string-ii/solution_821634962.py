# 0541 - Reverse String II
# Date: 2022-10-13
# Runtime: 76 ms, Memory: 14 MB
# Submission Id: 821634962


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_lst = list(s)
        def reverse(left, right):
            while left < right:
                s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
                left += 1
                right -= 1
                
        for i in range(0, len(s), 2*k):
            reverse(i, min(i+k, len(s))-1)
        return ''.join(s_lst)