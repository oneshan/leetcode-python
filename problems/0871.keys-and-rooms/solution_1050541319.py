# 0871 - Keys and Rooms
# Date: 2023-09-16
# Runtime: 75 ms, Memory: 17.3 MB
# Submission Id: 1050541319


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = {0}
        
        def dfs(curr):
            for neighbor in rooms[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        dfs(0)
        return len(seen) == n