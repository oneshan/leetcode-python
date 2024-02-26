# 1249 - Snapshot Array
# Date: 2023-06-11
# Runtime: 699 ms, Memory: 49.9 MB
# Submission Id: 968614957


class SnapshotArray:
    
    def __init__(self, length: int):
        self.snap_id = 0
        self.map = {idx: [[0, 0]] for idx in range(length)} # list of [snap_id, val]

    def set(self, index: int, val: int) -> None:
        if self.map[index][-1][0] == self.snap_id:
            self.map[index][-1][1] = val
        else:
            self.map[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.map[index]
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid
        return arr[left-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)