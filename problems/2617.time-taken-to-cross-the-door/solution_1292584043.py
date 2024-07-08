# 2617 - Time Taken to Cross the Door
# Date: 2024-06-19
# Runtime: 611 ms, Memory: 36.6 MB
# Submission Id: 1292584043


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        ENTER, EXIT = 0, 1

        queues = [deque(), deque()] # enter_queue, exit_queue
        ans = [-1] * len(arrival)

        curr_state = EXIT
        curr_time = 0
        i, n = 0, len(arrival)

        for _ in range(n):
            if i < n and not queues[0] and not queues[1] and arrival[i] > curr_time:
                curr_time = arrival[i]
                curr_state = EXIT
            
            while i < n and arrival[i] <= curr_time:
                queues[state[i]].append(i)
                i += 1

            if not queues[0] or not queues[1]:
                curr_state = ENTER if len(queues[1]) == 0 else EXIT
            
            idx = queues[curr_state].popleft()
            ans[idx] = curr_time
            curr_time += 1

        return ans