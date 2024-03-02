# 0211 - Design Add and Search Words Data Structure
# Date: 2024-03-01
# Runtime: 1711 ms, Memory: 64.4 MB
# Submission Id: 1190368315


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        candidates = [self.root]
        for ch in word:
            next_candidates = []
            for curr in candidates:
                if ch == '.':
                    next_candidates += curr.children.values()
                elif ch in curr.children:
                    next_candidates.append(curr.children[ch])
            if not next_candidates:
                return False
            candidates = next_candidates
        return any(curr.is_word for curr in candidates)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)