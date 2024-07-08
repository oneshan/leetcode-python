# 0588 - Design In-Memory File System
# Date: 2024-06-10
# Runtime: 49 ms, Memory: 16.9 MB
# Submission Id: 1283876381


class TrieNode:
    def __init__(self):
        self.child = {}
        self.content = None
        self.is_file = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        curr = self.root
        for sub in path.split('/'):
            if not sub:
                continue
            curr = curr.child[sub]

        if curr.is_file:
            return [sub]
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        curr = self.root
        for sub in path.split('/'):
            if not sub:
                continue
            if sub not in curr.child:
                curr.child[sub] = TrieNode()
            curr = curr.child[sub]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        for sub in filePath.split('/'):
            if not sub:
                continue
            if sub not in curr.child:
                curr.child[sub] = TrieNode()
            curr = curr.child[sub]

        if curr.content is None:
            curr.content = []
        curr.content.append(content)
        curr.is_file = True

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        for sub in filePath.split('/'):
            if not sub:
                continue
            if sub not in curr.child:
                return ''
            curr = curr.child[sub]
        return ''.join(curr.content)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)