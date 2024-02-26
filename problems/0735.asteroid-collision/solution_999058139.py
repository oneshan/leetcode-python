# 0735 - Asteroid Collision
# Date: 2023-07-20
# Runtime: 113 ms, Memory: 17.4 MB
# Submission Id: 999058139


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
                continue
                
            flag = True
            while stack and stack[-1] > 0:
                if stack[-1] < abs(num):
                    stack.pop()
                    continue
                if stack[-1] == abs(num):
                    stack.pop()
                flag = False
                break

            if flag:
                stack.append(num)
                
        return stack