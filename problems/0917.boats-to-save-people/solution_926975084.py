# 0917 - Boats to Save People
# Date: 2023-04-03
# Runtime: 460 ms, Memory: 20.9 MB
# Submission Id: 926975084


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        return boats