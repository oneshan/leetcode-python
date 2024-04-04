# 2213 - Find All People With Secret
# Date: 2024-03-25
# Runtime: 1653 ms, Memory: 93 MB
# Submission Id: 1213013134


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = {0, firstPerson}
        time_map = {}
        
        for x, y, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(set)
            time_map[t][x].add(y)
            time_map[t][y].add(x)
        
        def dfs(person):
            seen.add(person)
            stack = [person]
            while stack:
                p = stack.pop()
                secrets.add(p)
                for neighbor in time_map[t][p]:
                    if neighbor not in seen:
                        stack.append(neighbor)
                        seen.add(neighbor)

        for t in sorted(time_map.keys()):
            seen = set()
            for person in time_map[t]:
                if person in secrets:
                    dfs(person)
        return secrets