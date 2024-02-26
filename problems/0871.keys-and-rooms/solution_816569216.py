# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 87 ms, Memory: 14.8 MB
# Submission Id: 816569216


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set([0])
        def dfs(i):
            for j in rooms[i]:
                if j not in seen:
                    seen.add(j)
                    dfs(j)  
        dfs(0)
        return len(seen) == n