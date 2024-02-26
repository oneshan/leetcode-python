# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 186 ms, Memory: 14.6 MB
# Submission Id: 816557684


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set()
        stack = [0]
        while stack:
            p = stack.pop()
            seen.add(p)
            for q in rooms[p]:
                if q not in seen:
                    stack.append(q)
        return len(seen) == n