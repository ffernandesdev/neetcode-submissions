class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_buckets = [0, 0, 0]

        for c in nums:
            color_buckets[c] += 1

        j = 0

        for c in range(0, 3):
            for _ in range(color_buckets[c]):
                nums[j] = c
                j += 1
            