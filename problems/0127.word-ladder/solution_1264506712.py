# 0127 - Word Ladder
# Date: 2024-05-22
# Runtime: 150 ms, Memory: 34.3 MB
# Submission Id: 1264506712


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)

        len_s = len(wordList[0])
        graph = defaultdict(set)
        word_keys = defaultdict(set)
        for word in wordList + [beginWord]:
            for i in range(len_s):
                key = word[:i] + '_' + word[i+1:]
                graph[key].add(word)
                word_keys[word].add(key)

        ans = 0
        seen = set()
        queue = deque([beginWord])
        while queue:
            ans += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return ans
                for key in word_keys[word]:
                    for next_word in graph[key]:
                        if next_word not in seen:
                            seen.add(next_word)
                            queue.append(next_word)

        return 0
            