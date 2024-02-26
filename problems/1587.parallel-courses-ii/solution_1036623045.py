# 1587 - Parallel Courses II
# Date: 2023-08-31
# Runtime: 400 ms, Memory: 17.7 MB
# Submission Id: 1036623045


from collections import defaultdict

class Solution:    
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
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
            for k_courses in combinations(candidates, min(k, len(candidates))):
                next_mask = mask
                for course in k_courses:
                    next_mask |= 1 << course
                if next_mask not in seen:
                    seen.add(next_mask)
                    queue.append((next_mask, num_semesters + 1))
        return -1