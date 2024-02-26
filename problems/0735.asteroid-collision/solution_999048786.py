# 0735 - Asteroid Collision
# Date: 2023-07-20
# Runtime: 106 ms, Memory: 17.5 MB
# Submission Id: 999048786


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if num >= 0:
                stack.append(num)
                continue
            while stack and stack[-1] >= 0 and stack[-1] + num < 0:
                stack.pop()
            if stack and stack[-1] + num == 0:
                stack.pop()
                continue
            if not stack or stack[-1] < 0:
                stack.append(num)
                
        return stack