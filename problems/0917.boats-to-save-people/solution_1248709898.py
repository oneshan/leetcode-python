# 0917 - Boats to Save People
# Date: 2024-05-04
# Runtime: 330 ms, Memory: 23.4 MB
# Submission Id: 1248709898


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        ans = 0

        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            ans += 1

        if left == right:
            ans += 1
            
        return ans