# 0621 - Task Scheduler
# Date: 2024-03-19
# Runtime: 350 ms, Memory: 17 MB
# Submission Id: 1207974786


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_freq = max(counter.values())

        time = (n+1) * (max_freq-1)
        for task in counter:
            if counter[task] == max_freq:
                time += 1
        return max(len(tasks), time)