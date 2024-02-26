# 0745 - Find Smallest Letter Greater Than Target
# Date: 2023-06-09
# Runtime: 141 ms, Memory: 16.6 MB
# Submission Id: 967054369


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)-1
        target_val = ord(target)
        while left <= right:
            mid = (left + right) // 2
            value = ord(letters[mid])
            if value <= target_val:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left] if left < len(letters) else letters[0]