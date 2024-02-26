# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 167 ms, Memory: 14.3 MB
# Submission Id: 816561358


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = [False] * n
        stack = [0]
        while stack:
            p = stack.pop()
            seen[p] = True
            for q in rooms[p]:
                if not seen[q]:
                    stack.append(q)
        return all(seen)