# 2479 - Meeting Rooms III
# Date: 2022-10-09
# Runtime: 1576 ms, Memory: 59.7 MB
# Submission Id: 818223782


import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        records = [0] * n
        used_rooms = []  # heap: [end, room]
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:  # no free_rooms, delayed
                prev_end, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (prev_end + end - start, room))
            
            records[room] += 1                
        
        ans = 0
        for idx in range(n):
            if records[ans] < records[idx]:
                ans = idx
        return ans