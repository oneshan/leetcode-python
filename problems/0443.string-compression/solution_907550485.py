# 0443 - String Compression
# Date: 2023-03-02
# Runtime: 64 ms, Memory: 14.1 MB
# Submission Id: 907550485


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = j = 0
        while j < n:
            k = 0
            
            while j + k < n and chars[j] == chars[j+k]:
                k += 1
            chars[i], j = chars[j], j+k
            i += 1
            if k > 1:
                str_length = str(k)
                chars[i:i+len(str_length)] = list(str_length)
                i += len(str_length)
        return i