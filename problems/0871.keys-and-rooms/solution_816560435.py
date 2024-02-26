# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 151 ms, Memory: 14.5 MB
# Submission Id: 816560435


from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set()
        queue = deque([0])
        while queue:
            p = queue.popleft()
            seen.add(p)
            for q in rooms[p]:
                if q not in seen:
                    queue.append(q)
        return len(seen) == n