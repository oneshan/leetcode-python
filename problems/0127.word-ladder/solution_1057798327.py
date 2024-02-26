# 0127 - Word Ladder
# Date: 2023-09-24
# Runtime: 146 ms, Memory: 30.3 MB
# Submission Id: 1057798327


from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '_' + word[i+1:]
                graph[pattern].add(word)
                
        queue = deque([beginWord])
        seen = {beginWord}
        step = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    pattern = word[:i] + '_' + word[i+1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
            step += 1
        return 0