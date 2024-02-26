# 0127 - Word Ladder
# Date: 2022-12-01
# Runtime: 365 ms, Memory: 19.8 MB
# Submission Id: 852839897


from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        adj = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i]+'_'+word[i+1:]].add(word)
        
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                pattern = word[:i]+'_'+word[i+1:]
                for neighbor in adj[pattern] - seen:
                    seen.add(neighbor)
                    queue.append((neighbor, step+1))
        return 0