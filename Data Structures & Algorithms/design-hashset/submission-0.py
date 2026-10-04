class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        self.table[self._hash(key)].append(key)

    def remove(self, key: int) -> None:
        index = self._get_index(key)
        if index == -1:
            return
        
        bucket = self.table[self._hash(key)]
        bucket.pop(index)

    def contains(self, key: int) -> bool:
        return True if self._get_index(key) >= 0 else False
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def _get_index(self, key: int) -> int:
        bucket = self.table[self._hash(key)]

        for i, k in enumerate(bucket):
            if key == k:
                return i
        return -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)