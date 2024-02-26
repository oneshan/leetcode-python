# 2114 - Minimum Number of Work Sessions to Finish the Tasks
# Date: 2022-12-06
# Runtime: 5363 ms, Memory: 14 MB
# Submission Id: 855548084


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        sessions = []
        ans = n
        
        def dfs(idx):
            nonlocal ans
            if len(sessions) > ans:
                return
            if idx == n:
                ans = len(sessions)
                return
            for i in range(len(sessions)):
                if sessions[i] + tasks[idx] <= sessionTime:
                    sessions[i] += tasks[idx]
                    dfs(idx+1)
                    sessions[i] -= tasks[idx]

            sessions.append(tasks[idx])
            dfs(idx+1)
            sessions.pop()
        
        dfs(0)
        return ans