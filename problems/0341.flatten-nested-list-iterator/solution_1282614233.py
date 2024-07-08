# 0341 - Flatten Nested List Iterator
# Date: 2024-06-09
# Runtime: 41 ms, Memory: 19.2 MB
# Submission Id: 1282614233


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._generator = self._int_generator(nestedList)
        self._peek = None

    def _int_generator(self, nestedList):
        for obj in nestedList:
            if obj.isInteger():
                yield obj.getInteger()
            else:
                yield from self._int_generator(obj.getList())
    
    def next(self) -> int:
        if not self.hasNext:
            return None
        num = self._peek
        self._peek = None
        return num
    
    def hasNext(self) -> bool:
        if self._peek is None:
            self._peek = next(self._generator, None)
        return self._peek is not None
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())