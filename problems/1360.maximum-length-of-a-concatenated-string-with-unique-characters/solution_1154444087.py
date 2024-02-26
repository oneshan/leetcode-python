# 1360 - Maximum Length of a Concatenated String with Unique Characters
# Date: 2024-01-23
# Runtime: 83 ms, Memory: 16.5 MB
# Submission Id: 1154444087


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def get_mask(string):
            mask = 0
            for ch in string:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    return 0
                mask |= bit
            return mask
        
        def get_len(mask):
            res = 0
            while mask:
                mask &= (mask-1)
                res += 1
            return res
        
        arr = [get_mask(s) for s in arr]
        arr = [mask for mask in arr if mask]
        n = len(arr)
        
        def recur(i, mask):
            if i == n:
                return get_len(mask)
            res = get_len(mask)
            for j in range(i, n):
                if mask & arr[j] == 0:
                    res = max(res, recur(j+1, mask | arr[j]))
            return res
        
        return recur(0, 0)