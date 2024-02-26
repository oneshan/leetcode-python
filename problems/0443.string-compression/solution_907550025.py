# 0443 - String Compression
# Date: 2023-03-02
# Runtime: 63 ms, Memory: 14 MB
# Submission Id: 907550025


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = j = 0
        while j < n:
            k = 0
            
            prev = chars[j]
            while j < n and chars[j] == prev:
                j += 1
                k += 1

            chars[i] = prev
            i += 1
            if k > 1:
                str_length = str(k)
                chars[i:i+len(str_length)] = list(str_length)
                i += len(str_length)
        return i