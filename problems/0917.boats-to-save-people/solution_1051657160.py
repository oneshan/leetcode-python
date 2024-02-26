# 0917 - Boats to Save People
# Date: 2023-09-17
# Runtime: 395 ms, Memory: 23.2 MB
# Submission Id: 1051657160


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        
        ans = 0
        while left <= right:
            if people[right] > limit:
                break
            ans += 1
            if left == right:
                break
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
        return ans