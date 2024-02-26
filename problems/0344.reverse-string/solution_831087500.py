# 0344 - Reverse String
# Date: 2022-10-27
# Runtime: 577 ms, Memory: 43.4 MB
# Submission Id: 831087500


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        def recur(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            recur(left+1, right-1)
    
        recur(0, len(s)-1)