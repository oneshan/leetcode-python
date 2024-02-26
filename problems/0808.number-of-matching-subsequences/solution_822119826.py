# 0808 - Number of Matching Subsequences
# Date: 2022-10-14
# Runtime: 5947 ms, Memory: 16.9 MB
# Submission Id: 822119826


from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        table = defaultdict(list)
        for idx, ch in enumerate(s):
            table[ch].append(idx)
        
        def binary_search(array, target):
            left, right = 0, len(array)-1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == target:
                    return array[mid]
                if array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return array[left] if left < len(array) else -1
        
        def is_subsequences(word):
            curr_s = -1
            for idx, ch in enumerate(word):
                if ch not in table:
                    return False
                curr_s = binary_search(table[ch], curr_s+1)
                if curr_s == -1:
                    return False
            return True
                    

        ans = 0
        for word in words:
            ans += is_subsequences(word)
        return ans