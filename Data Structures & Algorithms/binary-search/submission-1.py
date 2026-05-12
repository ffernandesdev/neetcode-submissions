class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0;
        j = len(nums) - 1
        while i <= j:
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            i += 1
            j -= 1
        return -1