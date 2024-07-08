# 0269 - Alien Dictionary
# Date: 2024-05-25
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1267635232


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        unique_chars = set()
        for word in words:
            unique_chars |= set(word)

        n = len(words)
        for i in range(n-1):
            for c1, c2 in zip(words[i], words[i+1]):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        indegree[c2] += 1
                        graph[c1].add(c2)
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return ''
        
        queue = deque([ch for ch in unique_chars if indegree[ch] == 0])
        ans = []
        while queue:
            ch = queue.popleft()
            ans.append(ch)
            for next_ch in graph[ch]:
                indegree[next_ch] -= 1
                if indegree[next_ch] == 0:
                    queue.append(next_ch)

        return ''.join(ans) if len(ans) == len(unique_chars) else ''