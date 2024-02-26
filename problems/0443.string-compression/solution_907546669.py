# 0443 - String Compression
# Date: 2023-03-02
# Runtime: 58 ms, Memory: 14 MB
# Submission Id: 907546669


class Solution:
    def compress(self, chars: List[str]) -> int:
        
        def reverse(left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        n = len(chars)
        i = j = 0
        while j < n:
            k = t = 0
            
            prev = chars[j]
            while j < n and chars[j] == prev:
                j += 1
                k += 1

            chars[i] = prev
            i += 1
            if k == 1:
                continue

            while k:
                k, r = divmod(k, 10)
                chars[i+t] = str(r)
                t += 1
            reverse(i, i+t-1)
            i += t          
        return i