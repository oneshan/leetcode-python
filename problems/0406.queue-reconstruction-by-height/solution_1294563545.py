# 0406 - Queue Reconstruction by Height
# Date: 2024-06-20
# Runtime: 82 ms, Memory: 17.2 MB
# Submission Id: 1294563545


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans