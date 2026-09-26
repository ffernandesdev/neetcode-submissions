# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def internalQuickSort(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        l = s

        # partition: putting smaller elements to the left and greater or equal to the right
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[i], arr[l] = arr[l], arr[i]
                l += 1

        arr[l], arr[e] = pivot, arr[l]

        self.internalQuickSort(arr, s, l - 1)
        self.internalQuickSort(arr, l + 1, e)

        return arr

        

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.internalQuickSort(pairs, 0, len(pairs) - 1)
        