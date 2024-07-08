# 0406 - Queue Reconstruction by Height
# Date: 2024-06-20
# Runtime: 226 ms, Memory: 17 MB
# Submission Id: 1294567934


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))

        n = len(people)
        ans = [None] * n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if ans[j] is not None:
                    continue
                if cnt == people[i][1]:
                    ans[j] = people[i]
                    break
                cnt += 1
        return ans