# 0871 - Keys and Rooms
# Date: 2022-10-06
# Runtime: 133 ms, Memory: 14.4 MB
# Submission Id: 816561016


from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = [False] * n
        queue = deque([0])
        while queue:
            p = queue.popleft()
            seen[p] = True
            for q in rooms[p]:
                if not seen[q]:
                    queue.append(q)
        return all(seen)