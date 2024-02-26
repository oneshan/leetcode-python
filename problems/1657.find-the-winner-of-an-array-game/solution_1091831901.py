# 1657 - Find the Winner of an Array Game
# Date: 2023-11-05
# Runtime: 545 ms, Memory: 30.6 MB
# Submission Id: 1091831901


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        max_num = max(arr)
        
        queue = deque(arr)
        curr = queue.popleft()
        score = 0
        while queue:
            num = queue.popleft()
            if curr > num:
                queue.append(num)
                score += 1
            else:
                queue.append(curr)
                curr = num
                score = 1
                
            if score >= k or curr == max_num:
                return curr
            
        return curr