# 0017 - Letter Combinations of a Phone Number
# Date: 2022-12-05
# Runtime: 55 ms, Memory: 14 MB
# Submission Id: 855025779


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
                ans.append(''.join(arr[:]))
                return
            candidates = mapping[digits[idx]]
            for ch in candidates:
                arr[idx] = ch
                generate(arr, idx+1)
                
        generate(arr, 0)
        return ans