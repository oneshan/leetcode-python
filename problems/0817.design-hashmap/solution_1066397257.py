# 0817 - Design HashMap
# Date: 2023-10-04
# Runtime: 300 ms, Memory: 42.2 MB
# Submission Id: 1066397257


class MyHashMap:

    def __init__(self):
        self.arr = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)