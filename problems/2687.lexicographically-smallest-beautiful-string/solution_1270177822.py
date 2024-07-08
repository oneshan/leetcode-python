# 2687 - Lexicographically Smallest Beautiful String
# Date: 2024-05-28
# Runtime: 313 ms, Memory: 19.1 MB
# Submission Id: 1270177822


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        arr = [ord(ch) - ord('a') for ch in s]

        def is_palindrome(i, val):
            if i and arr[i-1] == val:
                return True
            if i > 1 and arr[i-2] == val:
                return True
            return False

        for i in range(n-1, -1, -1):
            if arr[i] == k-1:
                continue
            
            for j in range(arr[i]+1, k):
                if not is_palindrome(i, j):
                    arr[i] = j
                    break
            else:
                continue

            for j in range(i+1, n):
                arr[j] = next(t for t in range(k) if not is_palindrome(j, t))
            return ''.join(chr(val + ord('a')) for val in arr)
        
        return ''