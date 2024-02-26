# 0871 - Keys and Rooms
# Date: 2022-12-20
# Runtime: 200 ms, Memory: 14.4 MB
# Submission Id: 862703470


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        stack = [0]
        seen = {0}
        
        while stack:
            rid = stack.pop()
            for neighbor in rooms[rid]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return len(seen) == n