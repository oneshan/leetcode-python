# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 141 ms, Memory: 15 MB
# Submission Id: 816559196


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set()
        def dfs(i):
            seen.add(i)
            for j in rooms[i]:
                if j not in seen:
                    dfs(j)
        
        dfs(0)
        return len(seen) == n