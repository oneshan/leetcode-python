# 0648 - Replace Words
# Date: 2024-06-07
# Runtime: 102 ms, Memory: 33.6 MB
# Submission Id: 1280175911


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False
        self.word = None

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.is_word = True
        curr.word = word

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                break
            curr = curr.child[ch]
            if curr.is_word:
                return curr.word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = TrieTree()
        for word in dictionary:
            tree.insert(word)
        
        ans = []
        words = sentence.split()
        for word in words:
            root = tree.search(word)
            ans.append(root)
        return ' '.join(ans)