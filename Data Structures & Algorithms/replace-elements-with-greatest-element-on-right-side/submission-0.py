class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0, len(arr)):
            bigger = -1
            for j in range(i + 1, len(arr)):
                bigger = max(bigger, arr[j])
            arr[i] = bigger
        
        return arr
