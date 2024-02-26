# 1101 - Parallel Courses
# Date: 2023-08-31
# Runtime: 428 ms, Memory: 20 MB
# Submission Id: 1036624483


from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(int)        
        for _from, _to in relations:
            graph[_to-1] |= 1 << (_from-1)
                
        last_mask = (1 << n) - 1
        queue = deque([(0, 0)])
        seen = {0}
        while queue:
            mask, num_semesters = queue.popleft()
            if mask == last_mask:
                return num_semesters
            candidates = [i for i in range(n) if mask & (1 << i) == 0 and mask & graph[i] == graph[i]]
            next_mask = mask
            for course in candidates:
                next_mask |= 1 << course
            if next_mask not in seen:
                seen.add(next_mask)
                queue.append((next_mask, num_semesters + 1))
        return -1