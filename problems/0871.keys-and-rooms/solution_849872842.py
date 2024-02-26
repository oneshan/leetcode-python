# 0871 - Keys and Rooms
# Date: 2022-11-26
# Runtime: 77 ms, Memory: 14.3 MB
# Submission Id: 849872842


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        seen = set([0])
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        return len(seen) == n