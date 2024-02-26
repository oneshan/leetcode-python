# 1587 - Parallel Courses II
# Date: 2023-08-31
# Runtime: 944 ms, Memory: 18.1 MB
# Submission Id: 1036618422


from collections import defaultdict

class Solution:    
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for _from, _to in relations:
            graph[_from-1].add(_to-1)
            in_degree[_to-1] += 1
            
        @cache
        def backtrack(bit_mask):
            if not bit_mask:
                return 0
            
            candidates = [i for i in range(n) if in_degree[i] == 0 and bit_mask & (1 << i)]
            ans = float('inf')
            for k_courses in combinations(candidates, min(k, len(candidates))):
                next_mask = bit_mask                
                for course in k_courses:
                    next_mask ^= (1 << course)
                    for next_course in graph[course]:
                        in_degree[next_course] -= 1
                
                ans = min(ans, 1 + backtrack(next_mask))
                
                for course in k_courses:
                    for next_course in graph[course]:
                        in_degree[next_course] += 1                
            return ans
        
        return backtrack((1 << n) - 1) 