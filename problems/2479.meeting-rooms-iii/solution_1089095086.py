# 2479 - Meeting Rooms III
# Date: 2023-11-01
# Runtime: 1312 ms, Memory: 62.7 MB
# Submission Id: 1089095086


import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        records = [0] * n
        used_rooms = []
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
            else:
                ts, room = heapq.heappop(used_rooms)
                end += (ts - start)
                
            records[room] += 1
            heapq.heappush(used_rooms, (end, room))
        
        ans = 0
        for i in range(1, n):
            if records[ans] < records[i]:
                ans = i
        return ans