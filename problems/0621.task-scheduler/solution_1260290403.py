# 0621 - Task Scheduler
# Date: 2024-05-17
# Runtime: 487 ms, Memory: 17.1 MB
# Submission Id: 1260290403


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        max_heap = [-freq for freq in counter.values()]
        heapq.heapify(max_heap)
        queue = deque()  # [-freq, idle time]

        time = 0
        while max_heap or queue:
            time += 1

            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(max_heap, freq)

            if max_heap:
                freq = heapq.heappop(max_heap) + 1
                if freq:
                    queue.append((freq, time + n + 1))

        return time