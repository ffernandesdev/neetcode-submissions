class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.table = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index, bucket = self._get_bucket_and_index(key)
        entry = {
            "key": key,
            "value": value
        }

        if index == -1:
            bucket.append(entry)
        else:
            bucket[index] = entry

    def get(self, key: int) -> int:
        index, bucket = self._get_bucket_and_index(key)
        if index == -1:
            return -1
        
        return bucket[index]["value"]

    def remove(self, key: int) -> None:
        index, bucket = self._get_bucket_and_index(key)
        if index == -1:
            return

        bucket.pop(index)

    def _get_bucket_and_index(self, key: int) -> tuple[int, []]:
        bucket = self.table[self._hash(key)]

        for i, entry in enumerate(bucket):
            if key == entry["key"]:
                return [i, bucket]
        return [-1, bucket]

    def _hash(self, key: int) -> int:
        return key % self.size
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)