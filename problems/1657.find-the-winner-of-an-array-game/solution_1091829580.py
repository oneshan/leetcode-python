# 1657 - Find the Winner of an Array Game
# Date: 2023-11-05
# Runtime: 525 ms, Memory: 29.9 MB
# Submission Id: 1091829580


import heapq

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        curr, score = arr[0], 0
        for i in range(1, n):
            if curr > arr[i]:
                score += 1
            else:
                curr = arr[i]
                score = 1
                
            if score >= k:
                return curr
            
        return curr