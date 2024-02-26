# 1587 - Parallel Courses II
# Date: 2023-09-29
# Runtime: 1063 ms, Memory: 18.2 MB
# Submission Id: 1062102986


from collections import defaultdict, deque

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = defaultdict(int)
        for a, b in relations:
            graph[b-1] |= (1 << (a-1))
        
        def get_combinations(candidates, k):
            output = []
            def backtrack(arr, start, remains):
                if remains == 0:
                    output.append(arr[:])
                    return
                for i in range(start, len(candidates)):
                    arr.append(candidates[i])
                    backtrack(arr, i+1, remains-1)
                    arr.pop()
                    
            backtrack([], 0, k)
            return output
        
        last_mask = (1 << n) - 1
        queue = deque([0])
        seen = {0}
        num_semesters = 0
        while queue:
            for _ in range(len(queue)):
                mask = queue.popleft()
                if mask == last_mask:
                    return num_semesters
                candidates = [i for i in range(n) if mask & (1 << i) == 0 and mask & graph[i] == graph[i]]
                for courses in get_combinations(candidates, min(len(candidates), k)):
                    next_mask = mask
                    for course in courses:
                        next_mask |= (1 << course)
                    if next_mask not in seen:
                        seen.add(next_mask)
                        queue.append(next_mask)
            num_semesters += 1
        return -1