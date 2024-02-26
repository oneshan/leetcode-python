# 0017 - Letter Combinations of a Phone Number
# Date: 2023-08-03
# Runtime: 45 ms, Memory: 16.5 MB
# Submission Id: 1010889127


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        n = len(digits)
        arr = [''] * n
        
        def generate(arr, idx):
            if idx == n:
                ans.append(''.join(arr))
                return
            candidates = mapping[digits[idx]]
            for ch in candidates:
                arr[idx] = ch
                generate(arr, idx+1)
                
        generate(arr, 0)
        return ans