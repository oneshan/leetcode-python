# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 147 ms, Memory: 14.5 MB
# Submission Id: 816567689


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = [False] * n
        seen[0] = True
        stack = [0]
        
        while stack:
            p = stack.pop()
            for q in rooms[p]:
                if not seen[q]:
                    seen[q] = True
                    stack.append(q)
        return all(seen)