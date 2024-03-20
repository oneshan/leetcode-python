# 0621 - Task Scheduler
# Date: 2024-03-19
# Runtime: 411 ms, Memory: 17.2 MB
# Submission Id: 1207984860


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-freq for freq in counter.values()]
        heapq.heapify(heap)

        time = 0
        while heap:
            store = []
            task_count = min(len(heap), n+1)
            for _ in range(task_count):
                curr = -heapq.heappop(heap)
                if curr > 1:
                    store.append(-curr+1)
            for x in store:
                heapq.heappush(heap, x)

            time += task_count if not heap else n+1

        return time