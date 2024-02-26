# 2245 - Destroying Asteroids
# Date: 2022-10-10
# Runtime: 3844 ms, Memory: 27.9 MB
# Submission Id: 819169550


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid
        return True